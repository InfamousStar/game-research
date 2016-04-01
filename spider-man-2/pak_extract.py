#!/usr/bin/env python

import argparse

from os import makedirs
from struct import pack, unpack


def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
            help="print more to the console")
    parser.add_argument('-d', '--dry', action='store_true',
            help="don't actually write any files")
    parser.add_argument('pak', help="file to unpack")
    parser.add_argument('dest', default='extract', nargs='?',
            help="destination directory")
    args = parser.parse_args()

    with open(args.pak) as pak:
        print("File {} found.".format(args.pak))

        files = parsePakDir(pak)
        extractFiles(pak, args.dest, files)

        print("\nAll files extracted successfully!")


def parsePakDir(pak):
    """Returns information about files in given PAK archive.
    
    Arguments:
    pak -- file to parse

    Returns: list of dicts containing entries:
    'name' -- name of the file
    'type' -- whether the file is 'sound' or 'movie'
    'offset' -- offset of file in PAK
    'length' -- # of bytes in file
    """

    # get 1st file offset
    pak.seek(0x18)
    dataOffset = readInt16(pak)

    # get number of files
    pak.seek(0x4c)
    fileNum = readInt16(pak)

    # read file metadata
    pak.seek(0x258)

    files = []
    for i in range(fileNum):
        files.append({
            'name': pak.read(0x1f).strip('\0'),
            'type': 'sound' if (readInt8(pak) == 0x19) else 'movie',
            'offset': readInt32(pak) + dataOffset,
            'length': readInt32(pak)})

        if args.verbose:
            print(("file '{0[name]}' found").format(files[-1]))

    print("\n{} files found.\n".format(len(files)))

    return files


def extractFiles(pak, dest, files):
    """Extracts files to given directory.

    Args:
    pak -- file to unpack
    dest -- directory to extract to
    files -- dicts containing file metadata
    """

    # create directory
    # todo: make it not crash if dest exists
    if not args.dry:
        makedirs(dest)

    # pass files on
    for f in files:
        if f['type'] == 'sound':
            extractWaveBlock(pak, dest, f)
        else:
            extractMovie(pak, dest, f)


def extractWaveBlock(pak, dest, block):
    """Extract audio tracks from wave block.
    
    Args:
    pak -- file to extract from
    dest -- directory to extract to
    block -- dict containing block metadata
    """

    print("Extracting wave block '{0[name]}'...".format(block))

    # create block dest
    # todo: make it not crash if dest exist
    blockDest = dest + '/' + block['name']
    if not args.dry:
        makedirs(blockDest)

    tracks = parseBlockDir(pak, block)

    for track in tracks:
        extractTrack(pak, blockDest, track)


def extractMovie(pak, dest, movie):
    """Write movie stream to file.

    Args:
    pak -- file to extract from
    dest -- directory to extract to
    movie -- dict containing movie metadata
    """

    print("Extracting movie '{0[name]}'...".format(movie))

    # read movie
    pak.seek(movie['offset'])
    movie = pak.read(movie['length'])
    
    # write to file
    # todo: don't overwrite by default
    outPath = dest+'/'+movie['name']+'.ipu'
    if not args.dry:
        with open(outPath, 'w') as out:
            out.write(movie)


def parseBlockDir(pak, block):
    """Returns information about audio tracks in a wave block.
    
    Args:
    pak -- file to parse from
    block -- block metadata

    Returns: list of dicts containing entries:
    'name' -- name of the track
    'offset' -- offset of track's first byte
    'length' -- track length in bytes
    'rate' -- sample rate of the track
    """

    # get number of tracks
    pak.seek(block['offset']+0x40)
    trackNum = readInt32(pak)

    # get label offset
    pak.seek(block['offset']+0x64)
    labelOffset = readInt32(pak)

    # read track metadata
    infoPos = block['offset']+0x104
    labelPos = block['offset']+labelOffset

    tracks = []
    for i in range(trackNum):
        track = {}

        # read track info
        pak.seek(infoPos+0x4)
        track['length'] = readInt32(pak)
        pak.seek(0x10, 1)
        track['offset'] = readInt32(pak)+block['offset']
        track['rate'] = readInt32(pak)
        infoPos += 0x28

        # read track label
        pak.seek(labelPos)
        track['name'] = readUntilNull(pak)

        # skip the second label
        if i == 0: readUntilNull(pak)

        labelPos = pak.tell()  # move label position forward

        tracks.append(track)

        if args.verbose:
            print(("Track '{0[name]}' found.").format(track))

    if args.verbose:
        print("\n{} tracks found.\n".format(len(tracks)))

    return tracks


def extractTrack(pak, dest, track):
    """Write audio track to file.
    
    Args:
    pak -- file to extract from
    dest -- directory to extract to
    track -- dict containing track metadata
    """

    if args.verbose:
        print(("Extracting audio file '{0[name]}'...\n"
                "\tSample rate: {0[rate]}\n"
                "\tOffset: 0x{0[offset]:x}\n"
                "\tLength: 0x{0[length]:x}").format(track))

    # read track
    pak.seek(track['offset'])
    sound = pak.read(track['length'])

    # write to file
    outPath = dest+'/'+track['name']+'.ss2'
    if not args.dry:
        with open(outPath, 'w') as out:
            out.write(ss2Header(track))
            out.write(sound)


def ss2Header(track):
    """Returns the appropriate SS2 header for given audio track.
    I learned this header from the source code for vagguess, so thanks to Luigi
    Auriemma for that.
    
    Args:
    track -- dict containing track metadata
    """

    return pack('<4sIIIIIII4sI',
            'SShd',
            0x18,
            0x10,
            track['rate'],      # sample rate
            2,                  # channels
            0x800,              # interleave
            0,
            0xffffffff,         # disable loop
            'SSbd',
            track['length'])    # length


# These functions return the next 8/16/32 bits of a file as a little endian int.
def readInt8(f): return unpack('<b', f.read(1))[0]
def readInt16(f): return unpack('<h', f.read(2))[0]
def readInt32(f): return unpack('<l', f.read(4))[0]


def readUntilNull(f):
    """Reads data from the current position to the next null byte."""

    byte = ''
    s = ''
    while byte != '\0':
        s += byte
        byte = f.read(1)

    return s


if __name__ == '__main__':
    main()
