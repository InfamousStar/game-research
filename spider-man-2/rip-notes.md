Spider-Man 2 PS2 Rip Notes
==========================

* Music in SOUNDS.PAK
* Cinematics in MOVIES.PAK
* I can play the music in MFAudio with
    * File Format: RAW - Compressed ADPCM
    * Frequency: 44100 Hz
    * Samples: 16 bits
    * Channels: 2
    * Interleave: 0x800 bytes
    * Offset: 0x33296800 bytes
* [XeNTaX thread](forum.xentax.com/viewtopic.php?f=17&t=7258)

SOUNDS.PAK
----------
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

Music locations
---------------
* Most music in STREAMS_MUSIC
    * A lot of it is divided into intro, loop, ending
* Arcade jingles and Spider Eggs in interface block
    * Spider Eggs isn't missing from music block. I think this plays when you adjust music volume.
* Club, pizzaria music in ambient blocks; maybe more
    * Ambient 1
        * club alba
        * club redeye
    * Ambient 2
        * club kmfdm
        * club latin
        * msg lobby
        * mysterio apt
        * pizza shop (what is this song called?)
* FLYTHROUGH, ac64 Mysterio exp in misc block
* Cutscene music (w/ voice and sfx) in STREAMS_SCENE_EN
    * Spidey's girl
    * Final battle
    * Cat thief
    * Doc Ock bank ac77
    * War world
    * QB Triathlon ac80
    * Hello BC ac92
    * Poor Quentin
    * QB Triathlon ac97
    * Attract 1
    * Attract 2
    * Attract
    * Credits (no sfx yay!)
    * Finale
    * Hello
    * MNC
    * Opening Movie
    * Reactor Explosion
    * Peter Bday
    * Hello BC SA02
    * Meet Octavius
    * Black Cat Jewelry
    * Pride Octavius
    * Miss play
    * Birth Liz A
    * Birth Liz B
    * Birth Liz sa10
    * Birth of Lizard
    * sa12 Doc Ock Bank
    * sa15 Proposal
    * sa16 Hello Shock
    * sa17 Bye Shock A
    * sa20 Cat fun
    * sa21 BC breakup A
    * sa22 BC breakup B
    * sa23 Harry sells soul
    * sa24 Train fight
    * sa25 Train fight
    * sa26 Train fight C
    * sa26 Train fight D
    * sa27 Final battle
    * X-Men PAL
    * X-Men

Music notes
-----------
* Orchestra tracks @ 48kHz
* KMFDM tracks @ 44.1kHz
* Finiculi @ 32kHz
* Most tracks have a bit of silence at the end that messes up looping
    * I think this is because of the buffer size
* BC Chase 1 and 1b both work with ending 1
* Swing 2 loop 1 doesn't go with the ending
    * loop 2 doesn't go with the intro
* Swing us happy seems to have looping error within track, near beginning (replace w/ to the statue?)
* To the Statue is edit of swing us happy
* Finiculi jumps up a M3 as time runs out in-game
    * no slow-mo ending in files
* Hung Like a Spider loop 2 has intro
    * Ending goes w/ this intro
* Karacho's ending sounds ""
* Spider Eggs loop 2 has intro
* Mysterio doesn't loop well
* Ock Fight loop 1 is short version
    * loop 2 has intro
    * loop 3 is long version
    * ending is last timp hit of loop 3 w/ longer decay
* Thumpy is just a loop of the start of Karacho
* MP3 releases of KMFDM tracks
    * Pandemonium has longer intro
    * Suctioncups swaps start and end
    * Hung Like a Spider doubles intro
    * No song has an ending; they just cut off
* Credits contains 4 songs:
   * The Distillers' Spider-Man Theme
   * A version of Swing 1 with an ending
   * The Distillers - Beat Your Heart Out
   * A shortened version of BC Chase 2
