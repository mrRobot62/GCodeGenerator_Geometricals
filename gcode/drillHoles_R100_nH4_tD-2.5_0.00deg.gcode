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
G00 Z0010.000 F250.0 
(--- START HOLES ---)
  (--drill hole #00 at pos (100.0, 0.0) --) 
  G01 Z0003.000 F250.0 
  G01 X0100.000 Y0000.000 F250.0 
  (-- start Z loop total -2.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.000 F250.0 
  G01 Z-000.500 F150.0 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z-000.500 F250.0 
  G01 Z-001.000 F150.0 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-001.000 F250.0 
  G01 Z-001.500 F150.0 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.500 F250.0 
  G01 Z-002.000 F150.0 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-002.000 F250.0 
  G01 Z-002.500 F150.0 

  (-- end loop --)


  (--drill hole #01 at pos (0.0, 100.0) --) 
  G01 Z0003.000 F250.0 
  G01 X0000.000 Y0100.000 F250.0 
  (-- start Z loop total -2.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.000 F250.0 
  G01 Z-000.500 F150.0 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z-000.500 F250.0 
  G01 Z-001.000 F150.0 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-001.000 F250.0 
  G01 Z-001.500 F150.0 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.500 F250.0 
  G01 Z-002.000 F150.0 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-002.000 F250.0 
  G01 Z-002.500 F150.0 

  (-- end loop --)


  (--drill hole #02 at pos (-100.0, 0.0) --) 
  G01 Z0003.000 F250.0 
  G01 X-100.000 Y0000.000 F250.0 
  (-- start Z loop total -2.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.000 F250.0 
  G01 Z-000.500 F150.0 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z-000.500 F250.0 
  G01 Z-001.000 F150.0 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-001.000 F250.0 
  G01 Z-001.500 F150.0 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.500 F250.0 
  G01 Z-002.000 F150.0 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-002.000 F250.0 
  G01 Z-002.500 F150.0 

  (-- end loop --)


  (--drill hole #03 at pos (-0.0, -100.0) --) 
  G01 Z0003.000 F250.0 
  G01 X-000.000 Y-100.000 F250.0 
  (-- start Z loop total -2.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.000 F250.0 
  G01 Z-000.500 F150.0 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z-000.500 F250.0 
  G01 Z-001.000 F150.0 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-001.000 F250.0 
  G01 Z-001.500 F150.0 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.500 F250.0 
  G01 Z-002.000 F150.0 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-002.000 F250.0 
  G01 Z-002.500 F150.0 

  (-- end loop --)


(--- END HOLES ---)
(-- homeing --)
G01 Z0010.000 F300.0 
G01 X0000.000 Y0000.000 F300.0 
G00 Z10 F100 
M2

%
