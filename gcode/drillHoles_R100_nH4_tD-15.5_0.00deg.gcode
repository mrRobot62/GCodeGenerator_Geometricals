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
  G01 X0100.000 Y0000.000 Z0003.000 F250.0 
  (-- start Z loop total -15.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.500 F0250 
  G01 Z-000.500 F0150 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z0000.000 F0250 
  G01 Z-001.000 F0150 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-000.500 F0250 
  G01 Z-001.500 F0150 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.000 F0250 
  G01 Z-002.000 F0150 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-001.500 F0250 
  G01 Z-002.500 F0150 

  (-- new Z -003.000 --) 
  (retraction)
  G01 Z-002.000 F0250 
  G01 Z-003.000 F0150 

  (-- new Z -003.500 --) 
  (retraction)
  G01 Z-002.500 F0250 
  G01 Z-003.500 F0150 

  (-- new Z -004.000 --) 
  (retraction)
  G01 Z-003.000 F0250 
  G01 Z-004.000 F0150 

  (-- new Z -004.500 --) 
  (retraction)
  G01 Z-003.500 F0250 
  G01 Z-004.500 F0150 

  (-- new Z -005.000 --) 
  (retraction)
  G01 Z-004.000 F0250 
  G01 Z-005.000 F0150 

  (-- new Z -005.500 --) 
  (retraction)
  G01 Z-004.500 F0250 
  G01 Z-005.500 F0150 

  (-- new Z -006.000 --) 
  (retraction)
  G01 Z-005.000 F0250 
  G01 Z-006.000 F0150 

  (-- new Z -006.500 --) 
  (retraction)
  G01 Z-005.500 F0250 
  G01 Z-006.500 F0150 

  (-- new Z -007.000 --) 
  (retraction)
  G01 Z-006.000 F0250 
  G01 Z-007.000 F0150 

  (-- new Z -007.500 --) 
  (retraction)
  G01 Z-006.500 F0250 
  G01 Z-007.500 F0150 

  (-- new Z -008.000 --) 
  (retraction)
  G01 Z-007.000 F0250 
  G01 Z-008.000 F0150 

  (-- new Z -008.500 --) 
  (retraction)
  G01 Z-007.500 F0250 
  G01 Z-008.500 F0150 

  (-- new Z -009.000 --) 
  (retraction)
  G01 Z-008.000 F0250 
  G01 Z-009.000 F0150 

  (-- new Z -009.500 --) 
  (retraction)
  G01 Z-008.500 F0250 
  G01 Z-009.500 F0150 

  (-- new Z -010.000 --) 
  (retraction)
  G01 Z-009.000 F0250 
  G01 Z-010.000 F0150 

  (-- new Z -010.500 --) 
  (retraction)
  G01 Z-009.500 F0250 
  G01 Z-010.500 F0150 

  (-- new Z -011.000 --) 
  (retraction)
  G01 Z-010.000 F0250 
  G01 Z-011.000 F0150 

  (-- new Z -011.500 --) 
  (retraction)
  G01 Z-010.500 F0250 
  G01 Z-011.500 F0150 

  (-- new Z -012.000 --) 
  (retraction)
  G01 Z-011.000 F0250 
  G01 Z-012.000 F0150 

  (-- new Z -012.500 --) 
  (retraction)
  G01 Z-011.500 F0250 
  G01 Z-012.500 F0150 

  (-- new Z -013.000 --) 
  (retraction)
  G01 Z-012.000 F0250 
  G01 Z-013.000 F0150 

  (-- new Z -013.500 --) 
  (retraction)
  G01 Z-012.500 F0250 
  G01 Z-013.500 F0150 

  (-- new Z -014.000 --) 
  (retraction)
  G01 Z-013.000 F0250 
  G01 Z-014.000 F0150 

  (-- new Z -014.500 --) 
  (retraction)
  G01 Z-013.500 F0250 
  G01 Z-014.500 F0150 

  (-- new Z -015.000 --) 
  (retraction)
  G01 Z-014.000 F0250 
  G01 Z-015.000 F0150 

  (-- new Z -015.500 --) 
  (retraction)
  G01 Z-014.500 F0250 
  G01 Z-015.500 F0150 

  (-- end loop --)


  (--drill hole #01 at pos (0.0, 100.0) --)
  G01 X0000.000 Y0100.000 Z0003.000 F250.0 
  (-- start Z loop total -15.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.500 F0250 
  G01 Z-000.500 F0150 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z0000.000 F0250 
  G01 Z-001.000 F0150 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-000.500 F0250 
  G01 Z-001.500 F0150 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.000 F0250 
  G01 Z-002.000 F0150 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-001.500 F0250 
  G01 Z-002.500 F0150 

  (-- new Z -003.000 --) 
  (retraction)
  G01 Z-002.000 F0250 
  G01 Z-003.000 F0150 

  (-- new Z -003.500 --) 
  (retraction)
  G01 Z-002.500 F0250 
  G01 Z-003.500 F0150 

  (-- new Z -004.000 --) 
  (retraction)
  G01 Z-003.000 F0250 
  G01 Z-004.000 F0150 

  (-- new Z -004.500 --) 
  (retraction)
  G01 Z-003.500 F0250 
  G01 Z-004.500 F0150 

  (-- new Z -005.000 --) 
  (retraction)
  G01 Z-004.000 F0250 
  G01 Z-005.000 F0150 

  (-- new Z -005.500 --) 
  (retraction)
  G01 Z-004.500 F0250 
  G01 Z-005.500 F0150 

  (-- new Z -006.000 --) 
  (retraction)
  G01 Z-005.000 F0250 
  G01 Z-006.000 F0150 

  (-- new Z -006.500 --) 
  (retraction)
  G01 Z-005.500 F0250 
  G01 Z-006.500 F0150 

  (-- new Z -007.000 --) 
  (retraction)
  G01 Z-006.000 F0250 
  G01 Z-007.000 F0150 

  (-- new Z -007.500 --) 
  (retraction)
  G01 Z-006.500 F0250 
  G01 Z-007.500 F0150 

  (-- new Z -008.000 --) 
  (retraction)
  G01 Z-007.000 F0250 
  G01 Z-008.000 F0150 

  (-- new Z -008.500 --) 
  (retraction)
  G01 Z-007.500 F0250 
  G01 Z-008.500 F0150 

  (-- new Z -009.000 --) 
  (retraction)
  G01 Z-008.000 F0250 
  G01 Z-009.000 F0150 

  (-- new Z -009.500 --) 
  (retraction)
  G01 Z-008.500 F0250 
  G01 Z-009.500 F0150 

  (-- new Z -010.000 --) 
  (retraction)
  G01 Z-009.000 F0250 
  G01 Z-010.000 F0150 

  (-- new Z -010.500 --) 
  (retraction)
  G01 Z-009.500 F0250 
  G01 Z-010.500 F0150 

  (-- new Z -011.000 --) 
  (retraction)
  G01 Z-010.000 F0250 
  G01 Z-011.000 F0150 

  (-- new Z -011.500 --) 
  (retraction)
  G01 Z-010.500 F0250 
  G01 Z-011.500 F0150 

  (-- new Z -012.000 --) 
  (retraction)
  G01 Z-011.000 F0250 
  G01 Z-012.000 F0150 

  (-- new Z -012.500 --) 
  (retraction)
  G01 Z-011.500 F0250 
  G01 Z-012.500 F0150 

  (-- new Z -013.000 --) 
  (retraction)
  G01 Z-012.000 F0250 
  G01 Z-013.000 F0150 

  (-- new Z -013.500 --) 
  (retraction)
  G01 Z-012.500 F0250 
  G01 Z-013.500 F0150 

  (-- new Z -014.000 --) 
  (retraction)
  G01 Z-013.000 F0250 
  G01 Z-014.000 F0150 

  (-- new Z -014.500 --) 
  (retraction)
  G01 Z-013.500 F0250 
  G01 Z-014.500 F0150 

  (-- new Z -015.000 --) 
  (retraction)
  G01 Z-014.000 F0250 
  G01 Z-015.000 F0150 

  (-- new Z -015.500 --) 
  (retraction)
  G01 Z-014.500 F0250 
  G01 Z-015.500 F0150 

  (-- end loop --)


  (--drill hole #02 at pos (-100.0, 0.0) --)
  G01 X-100.000 Y0000.000 Z0003.000 F250.0 
  (-- start Z loop total -15.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.500 F0250 
  G01 Z-000.500 F0150 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z0000.000 F0250 
  G01 Z-001.000 F0150 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-000.500 F0250 
  G01 Z-001.500 F0150 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.000 F0250 
  G01 Z-002.000 F0150 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-001.500 F0250 
  G01 Z-002.500 F0150 

  (-- new Z -003.000 --) 
  (retraction)
  G01 Z-002.000 F0250 
  G01 Z-003.000 F0150 

  (-- new Z -003.500 --) 
  (retraction)
  G01 Z-002.500 F0250 
  G01 Z-003.500 F0150 

  (-- new Z -004.000 --) 
  (retraction)
  G01 Z-003.000 F0250 
  G01 Z-004.000 F0150 

  (-- new Z -004.500 --) 
  (retraction)
  G01 Z-003.500 F0250 
  G01 Z-004.500 F0150 

  (-- new Z -005.000 --) 
  (retraction)
  G01 Z-004.000 F0250 
  G01 Z-005.000 F0150 

  (-- new Z -005.500 --) 
  (retraction)
  G01 Z-004.500 F0250 
  G01 Z-005.500 F0150 

  (-- new Z -006.000 --) 
  (retraction)
  G01 Z-005.000 F0250 
  G01 Z-006.000 F0150 

  (-- new Z -006.500 --) 
  (retraction)
  G01 Z-005.500 F0250 
  G01 Z-006.500 F0150 

  (-- new Z -007.000 --) 
  (retraction)
  G01 Z-006.000 F0250 
  G01 Z-007.000 F0150 

  (-- new Z -007.500 --) 
  (retraction)
  G01 Z-006.500 F0250 
  G01 Z-007.500 F0150 

  (-- new Z -008.000 --) 
  (retraction)
  G01 Z-007.000 F0250 
  G01 Z-008.000 F0150 

  (-- new Z -008.500 --) 
  (retraction)
  G01 Z-007.500 F0250 
  G01 Z-008.500 F0150 

  (-- new Z -009.000 --) 
  (retraction)
  G01 Z-008.000 F0250 
  G01 Z-009.000 F0150 

  (-- new Z -009.500 --) 
  (retraction)
  G01 Z-008.500 F0250 
  G01 Z-009.500 F0150 

  (-- new Z -010.000 --) 
  (retraction)
  G01 Z-009.000 F0250 
  G01 Z-010.000 F0150 

  (-- new Z -010.500 --) 
  (retraction)
  G01 Z-009.500 F0250 
  G01 Z-010.500 F0150 

  (-- new Z -011.000 --) 
  (retraction)
  G01 Z-010.000 F0250 
  G01 Z-011.000 F0150 

  (-- new Z -011.500 --) 
  (retraction)
  G01 Z-010.500 F0250 
  G01 Z-011.500 F0150 

  (-- new Z -012.000 --) 
  (retraction)
  G01 Z-011.000 F0250 
  G01 Z-012.000 F0150 

  (-- new Z -012.500 --) 
  (retraction)
  G01 Z-011.500 F0250 
  G01 Z-012.500 F0150 

  (-- new Z -013.000 --) 
  (retraction)
  G01 Z-012.000 F0250 
  G01 Z-013.000 F0150 

  (-- new Z -013.500 --) 
  (retraction)
  G01 Z-012.500 F0250 
  G01 Z-013.500 F0150 

  (-- new Z -014.000 --) 
  (retraction)
  G01 Z-013.000 F0250 
  G01 Z-014.000 F0150 

  (-- new Z -014.500 --) 
  (retraction)
  G01 Z-013.500 F0250 
  G01 Z-014.500 F0150 

  (-- new Z -015.000 --) 
  (retraction)
  G01 Z-014.000 F0250 
  G01 Z-015.000 F0150 

  (-- new Z -015.500 --) 
  (retraction)
  G01 Z-014.500 F0250 
  G01 Z-015.500 F0150 

  (-- end loop --)


  (--drill hole #03 at pos (-0.0, -100.0) --)
  G01 X-000.000 Y-100.000 Z0003.000 F250.0 
  (-- start Z loop total -15.5 step -0.5--) 
  (-- new Z -000.500 --) 
  (retraction)
  G01 Z0000.500 F0250 
  G01 Z-000.500 F0150 

  (-- new Z -001.000 --) 
  (retraction)
  G01 Z0000.000 F0250 
  G01 Z-001.000 F0150 

  (-- new Z -001.500 --) 
  (retraction)
  G01 Z-000.500 F0250 
  G01 Z-001.500 F0150 

  (-- new Z -002.000 --) 
  (retraction)
  G01 Z-001.000 F0250 
  G01 Z-002.000 F0150 

  (-- new Z -002.500 --) 
  (retraction)
  G01 Z-001.500 F0250 
  G01 Z-002.500 F0150 

  (-- new Z -003.000 --) 
  (retraction)
  G01 Z-002.000 F0250 
  G01 Z-003.000 F0150 

  (-- new Z -003.500 --) 
  (retraction)
  G01 Z-002.500 F0250 
  G01 Z-003.500 F0150 

  (-- new Z -004.000 --) 
  (retraction)
  G01 Z-003.000 F0250 
  G01 Z-004.000 F0150 

  (-- new Z -004.500 --) 
  (retraction)
  G01 Z-003.500 F0250 
  G01 Z-004.500 F0150 

  (-- new Z -005.000 --) 
  (retraction)
  G01 Z-004.000 F0250 
  G01 Z-005.000 F0150 

  (-- new Z -005.500 --) 
  (retraction)
  G01 Z-004.500 F0250 
  G01 Z-005.500 F0150 

  (-- new Z -006.000 --) 
  (retraction)
  G01 Z-005.000 F0250 
  G01 Z-006.000 F0150 

  (-- new Z -006.500 --) 
  (retraction)
  G01 Z-005.500 F0250 
  G01 Z-006.500 F0150 

  (-- new Z -007.000 --) 
  (retraction)
  G01 Z-006.000 F0250 
  G01 Z-007.000 F0150 

  (-- new Z -007.500 --) 
  (retraction)
  G01 Z-006.500 F0250 
  G01 Z-007.500 F0150 

  (-- new Z -008.000 --) 
  (retraction)
  G01 Z-007.000 F0250 
  G01 Z-008.000 F0150 

  (-- new Z -008.500 --) 
  (retraction)
  G01 Z-007.500 F0250 
  G01 Z-008.500 F0150 

  (-- new Z -009.000 --) 
  (retraction)
  G01 Z-008.000 F0250 
  G01 Z-009.000 F0150 

  (-- new Z -009.500 --) 
  (retraction)
  G01 Z-008.500 F0250 
  G01 Z-009.500 F0150 

  (-- new Z -010.000 --) 
  (retraction)
  G01 Z-009.000 F0250 
  G01 Z-010.000 F0150 

  (-- new Z -010.500 --) 
  (retraction)
  G01 Z-009.500 F0250 
  G01 Z-010.500 F0150 

  (-- new Z -011.000 --) 
  (retraction)
  G01 Z-010.000 F0250 
  G01 Z-011.000 F0150 

  (-- new Z -011.500 --) 
  (retraction)
  G01 Z-010.500 F0250 
  G01 Z-011.500 F0150 

  (-- new Z -012.000 --) 
  (retraction)
  G01 Z-011.000 F0250 
  G01 Z-012.000 F0150 

  (-- new Z -012.500 --) 
  (retraction)
  G01 Z-011.500 F0250 
  G01 Z-012.500 F0150 

  (-- new Z -013.000 --) 
  (retraction)
  G01 Z-012.000 F0250 
  G01 Z-013.000 F0150 

  (-- new Z -013.500 --) 
  (retraction)
  G01 Z-012.500 F0250 
  G01 Z-013.500 F0150 

  (-- new Z -014.000 --) 
  (retraction)
  G01 Z-013.000 F0250 
  G01 Z-014.000 F0150 

  (-- new Z -014.500 --) 
  (retraction)
  G01 Z-013.500 F0250 
  G01 Z-014.500 F0150 

  (-- new Z -015.000 --) 
  (retraction)
  G01 Z-014.000 F0250 
  G01 Z-015.000 F0150 

  (-- new Z -015.500 --) 
  (retraction)
  G01 Z-014.500 F0250 
  G01 Z-015.500 F0150 

  (-- end loop --)


(--- END HOLES ---)
G01 X0000.000 Y0000.000 Z0010.000 F300.0 
G00 Z10 F100 
M2

%
