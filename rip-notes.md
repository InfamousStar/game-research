Spider-Man 2 Rip Notes
======================

PS2
---
* Music in SOUNDS.PAK
* Cinematics in MOVIES.PAK
* I can play the music in MFAudio with
    * File Format: RAW - Compressed ADPCM
    * Frequency: 44100 Hz
    * Samples: 16 bits
    * Channels: 2
    * Interleave: 0x800 bytes
    * Offset: 0x33296800 bytes
* XeNTaX thread: forum.xentax.com/viewtopic.php?f=17&t=7258

### SOUNDS.PAK ###
* Divided into blocks, each starting with 'WAVEBK11'
* start of 1st block @ 0x18 (same in movies)
* # of blocks at 0x4c (same in MOVIES.PAK) & 0x1dc (@ 0x1e0 in MOVIES.PAK)
* Block info starts at 0x258 (same w/ MOVIES.PAK)
    * preceded by E3 E3 E3 E3 00 00 00 00 E3 E3 E3 E3 
    * each entry is 40B
        * 31B name
        * 0x19 (0x1A in movies)
        * uint32 offset starting from 1st block @ 0x1800 (0x800 in movies)
        * uint32 block size (last block cut off)

* Music block begins at offset 0x33295800
* Block reads:
    'WAVEBK11'
    (9 null bytes) 10 (6 null bytes)
    00 10 00 00 (offset from start of block to 1st track?)
    00 50 E5 0A (length of block minus end padding)
    'STREAMS_MUSIC'
* track info starts at 0x33295904
    * each entry is 40B
        * 04 12 (or 1A) 03 00
        * uint32 length
        * 12 bytes unknown
        * FF FF FF FF
        * uint32 offset
        * uint32 sample rate
        * 8 bytes unknown
* Eventually there are labels, which are null-terminated strings
    * 2nd label is just a shorter version of the block name
* Audio streams start at 0x33295800
    * According to distortedximage on xentax, they're in mib format
* 50? streams

* A couple other tracks in interface block
    * Arcade jingles and spider eggs (which isn't missing from the music block. I think this version plays when you adjust the music volume)
* Club, pizzaria music in ambient block; maybe more

### PAK format ###
This information applies to SOUNDS.PAK and MOVIES.PAK. AMALGA.PAK and
rmalga.pak seem to be in a different format (except for the 1st 24 bytes). They
also seem to be the same file.

PAK archives store files in a directory-data format. They begin with:

Offset  Size    Description
0x0     24      0B 00 00 00 D6 03 00 00 33 03 00 00
                97 01 00 00 00 00 00 00 30 00 00 00
0x18    uint16  offset of 1st file
0x4C    uint8   number of files
0x258           directory

The directory consists of 40B entries, each one looking like this:

Offset  Size    Description
+0x0    31      file name
+0x1f   1       unknown (might indicate file type; 19 in SOUNDS, 1A in MOVIES)
+0x20   uint32  file offset (from start of 1st file)
+0x24   uint32  file length

The files in MOVIES.PAK start out with the signature 'ipum' and the rest, I
assume, is compressed video. In SOUNDS.PAK, the files are archives themselves,
each one storing a collection of related audio tracks. Because of their file
signature, I call them 'wave blocks' or just 'blocks'. Blocks have a different
format from PAKs, in which the directory is split up between track info, and
names. Blocks can have one of two headers, but if you'll notice, everything
needed to extract the audio is in the same place:

Offset  Size    Description
+0x0    8       file signature 'WAVEBK11'
+0x10   uint32  data offset (from start of block)
+0x14   uint32  data length (sans padding)
+0x18   uint32  block length
+0x1c   4       padding
+0x20   32      block name
+0x40   uint16  number of tracks
+0x44   32      unknown
+0x64   uint32  label offset
+0x68   156     unknown (padding?)
+0x104          track info

or

Offset  Size    Description
+0x0    8       file signature 'WAVEBK11'
+0x8    8       padding
+0x10   uint32  data offset (from start of block)
+0x14   4       padding
+0x18   uint32  data offset (again)
+0x1c   uint32  data length (w/ padding)
+0x20   32      block name
+0x40   uint32  number of tracks
+0x44   32      unknown
+0x64   uint32  label offset
+0x68   156     unknown (padding?)
+0x104          track info

In the info part of the directory, each track gets a 40B entry:

Offset  Size    Description
+0x0    4       unknown, starts with 0x04
+0x4    uint32  track length (in bytes obviously, not seconds)
+0x8    12      unknown
+0x14   4       FF FF FF FF (not sure why)
+0x18   uint32  track offset
+0x1c   uint32  sample rate
+0x20   8       unknown

The name part is a series of null-terminated strings. As best I can tell,
there's always 1 more label than there are tracks, the 2nd label being a
shorter version of the block's name. I don't know why. The tracks themselves
are compressed ADPCM with an interleave of 0x800.
