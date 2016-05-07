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

Where songs appear in-game
--------------------------
* Flythrough
* a67 spidey's girl
* Opening Movie
* Swing 1 short (to dr connor's class)
* Suctioncups (briefcase fight)
* Spider Eggs (going to meet mj)
* ac92 Hello BC (mj has a bf)
* Kaboom (art thieves)
* sa02 hello bc
* bc chase 1
* swing 1 full (pics for robbie)
* Arachnophiliac (rhino fight)
* Swing 2-1 (right before you get to ock's apt)
* sa04 Meet Octavius
* BC Chase 1b
* sa07 black cat jewelry
* thumpy (beck stadium foyer)
* ac80 qb triathlon
* organ music charge 1
* organ music charge 2
* ac97 qb triathlon
* sa08 pride octavius
* swing 1 full (get to mj's play)
* arachnophiliac (picked a bad night)
* sa09 miss play
* BC Chase 1
* ac72 catthief
* Arachnophiliac (fighting art thieves)
* MNC (enter mysterio)
* Swing 2-2
* ac64 Mysterio Exp
* Mysterio
* Swing 2-1
* To the Statue
* Mysterio
* ac79 war world
* bg mysterio apt int
* reactor explosion
* vertical dilemma
* Webhed (mysterio robo ambush)
* sa10 birthliz/a/birth of lizard
* sa10 birthliz b
* sa12 doc ock bank
* ock fight 1
* ac77 doc ock bank
* hung like a spider 2 (fighting ock's goons)
* silhouettes (chasing the chopper)
* swing 1 (right outside peter's apt)
* sa15 proposal
* BC Chase 2
* karacho (shocker fight)
* sa16 hello shock
* ac93 poor quentin
* sa17 bye shock a
* bc chase 2
* Karacho (shocker fight again)
* swing 2-2 (mj's play again)
* swing 1 (bc's at the chrysler building)
* bc chase 2
* sa20 cat fun
* Hairy legs
* swing 2-2 (need to have a talk w/ bc)
* sa21 bc breakup a
* swing 2-2 (mj love confession)
* sa22 bc breakup b
* sa23 harry sells soul
* swing 2-1 (to mj's diner)
* sa24 train fight
* swing 2-2
* sa25 train fight
* ock fight 1
* sa26 train fight c
* sa26 train fight d
* swing 2-1
* sa27 final battle
* vertical dilemma
* ac69 final bat
* ock fight 2
* finale
* credits

Cues and cutscenes
------------------
* Flythrough - Flythrough
* ac67 - Flythrough (end), More Girl Trouble (start)
* Opening Movie - Opening`(Swing?)
* ac92 - Love theme (short) + tension
* sa02 - Hello BC
* sa04 - Meeting Octavius
* sa07 - BC convo 1
* ac80 - Thumpy, Charge, Thumpy
* ac97 - Mysterio (excerpt)
* sa08 - Octavius' Pride
* sa09 - Spidey's Girl Trouble
* ac72 - Hello BC (start)
* mnc - Mysterio (start)
* ac64 - Theremin
* ac79 - Flythrough (excerpts)
* Reactor Explosion - Reactor Explosion
* sa10a - Birth of Lizard
* sa10b - Pete Finds Connors
* sa12 - Ock's Bank Robbery
* ac77 - Ock fight 2 (start)
* sa15 - More Girl Trouble (Only one spider-man?)
* sa16 - BC Gets Shocked
* ac93 - theremin
* sa17 - Spidey vs JJ
* sa20 - Hello BC (excerpts)
* sa21 - Breaking up w/ BC
* sa22 - Love theme
* sa23 - Harry Sells His Soul
* sa24 - The Diner
* sa25 - Ock Boards a train
* sa26c&d - Spidey Stops a Train, Harry's revelation
* sa27 - Ock's reactor, Ock's presence
* ac69 - Harry Sells His Soul (excerpts)
* finale - Octavius Dies, PP and MJ, MJ chooses PP
* credits - Spider-Man Theme, Swing 1, Beat Your Heart Out, BC Chase 2

* sa25, 0:11-0:16 is from sa23

Tentative tracklist
-------------------
* 'Overture' from flythrough
* 'The City's Been Quiet Lately' from openingmovie
* 'Suctioncups' from mx_suctioncups
* 'Spider Eggs' from mx_spidereggs_loop, "ending
* 'MJ has a Boyfriend' from ac92
* 'Kaboom' from mx_kaboom, "end
* 'Hello Black Cat' from sa02, ac72, sa20
* 'Black Cat Chase 1' from mx_bcchase1..., mx_bcchase_ending1
* 'Swing From a Thread' from credits
* 'Arachnophiliac' from mx_arachnophiliac
* 'Meeting Octavius' from sa04
* 'Black Cat Chase 2' from mx_bcchase1b_intro, "loop, mx_bcchase_ending1
* 'Black Cat Crossed Your Path' from sa07
* 'Octavius' Pride' from sa08
* 'Peeping Tom Routine' from sa09
* 'Mysterio' from mx_mysterio_loop
* 'Take a Look Overhead (ver. 2)' from mx_swing2_loop2
* 'Take a Look Overhead (ver. 1)' from mx_swing2_intro, "loop1
* 'Reactor Explosion' from reactorexplosion
* 'Vertical Dilemma' from mx_verticaldilemma
* 'Webhed' from mx_webhed
* 'Enter Doc Ock' from sa10a, b
* 'Hung Like a Spider' from mx_hunglikeaspider_loop2
* 'Silhouettes' from mx_silhouettes
* 'He Threw a Football on the Moon' from sa15
* 'Black Cat Chase 3' from credits
* 'Karacho' from mx_karacho_loop, "end
* 'Black Cat Gets Shocked' from sa16
* 'Spidey vs JJ' from sa17
* 'Take a Look Overhead (ver. 2)' from mx_swing2_loop2
* 'Hairy Legs' from mx_hairylegs_loop, "end
* 'Breaking Up With Cat' from sa21
* 'Confessing to Mary Jane' from sa22
* 'Harry Sells His Soul' from sa23, sa25
* 'Mary Jane Kidnapped' from sa24
* 'Ock Boards a Train' from sa25
* 'Harry's Revelation' from sa26c, d
* 'Ock's Masterpiece Recreated' from sa27
* 'Ock Fight' from mx_ockfight_loop1, "loop2, "end
* 'Octavius Dies' from finale
* 'Peter Lets MJ Go' from finale
* 'Go Get 'em, Tiger' from finale
* 'Theme From Spider-Man' from credits
* 'Beat Your Heart Out' from credits
* 'Pandemonium' from mx_pandemonium
* 'Web of Intrigue' from mx_webofintrigue
* 'Hello' from hello
* 'Alba Club Music' from bg_club_alba_int
* 'Redeye Club Music' from bg_club_redeye_int
* 'Latin Club Music' from bg_club_latin_int
* 'Funiculi, Funicula' from mx_finiculi
* 'Tarantella Napolitana' from bg_pizzashop_int
* 'Charge! (Ver. 1)' from s10_organmusic_charge_1
* 'Charge! (Ver. 2)' from s10_organmusic_charge_2
* 'Theremin Blast 1' from mx_thereminblast_1
* 'Theremin Blast 2' from ac64
* 'Arcade Start' from arc_music_startgame
* 'Arcade Game Over' from arc_music_gameover
