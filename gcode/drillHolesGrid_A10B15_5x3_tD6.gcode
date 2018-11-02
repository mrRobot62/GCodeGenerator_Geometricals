%
(--------------------------)
(          __              )
(  _(\    |@@|             )
( (__/\__ \--/ __          )
(    \___|----|  |   __    )
(        \ }{ /\ )_ / _\   )
(        /\__/\ \__O (__   )
(       (--/\--)    \__/   )
(       _)(  )(_           )
(      `---''---`          )
(    (c) by LunaX 2018     )
(--------------------------)
        

(set ContourHoles preamble)
G21 G90 G64 G17 G40 G49
G21

(set Z saftey position)
G00 Z0010.000 F200.0 

(--- START DRILL HOLES ---)
 (--Hole #01 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0000.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0000.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #02 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0020.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0020.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #03 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0040.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0040.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #04 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0060.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0060.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #05 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0080.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0080.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #06 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0000.000 Y0015.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0000.000 Y0015.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #07 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0020.000 Y0015.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0020.000 Y0015.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #08 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0040.000 Y0015.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0040.000 Y0015.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #09 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0060.000 Y0015.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0060.000 Y0015.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #10 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0080.000 Y0015.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0080.000 Y0015.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #11 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0000.000 Y0030.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0000.000 Y0030.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #12 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0020.000 Y0030.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0020.000 Y0030.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #13 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0040.000 Y0030.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0040.000 Y0030.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #14 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0060.000 Y0030.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0060.000 Y0030.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #15 at angle 000.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0080.000 Y0030.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0080.000 Y0030.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

(--- END DRILL HOLES ---)
G01 Z0010.000 F200.0 
G01 X0000.000 Y0000.000 F200.0 
G00 Z10 F100 
M2

%
