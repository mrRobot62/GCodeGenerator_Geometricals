%

(set ContourHoles preamble)
G21 G90 G64 G17 G40 G49
G21

(set Z saftey position)
G00 Z0010.000 F250.0 
(--- START HOLES ---)
  (--drill hole #00 at pos (96.593, 25.882) --)
  G01 X0096.593 Y0025.882 Z0003.000 F250.0 
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


  (--drill hole #01 at pos (70.711, 70.711) --)
  G01 X0070.711 Y0070.711 Z0003.000 F250.0 
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


  (--drill hole #02 at pos (25.882, 96.593) --)
  G01 X0025.882 Y0096.593 Z0003.000 F250.0 
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


  (--drill hole #03 at pos (-25.882, 96.593) --)
  G01 X-025.882 Y0096.593 Z0003.000 F250.0 
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


  (--drill hole #04 at pos (-70.711, 70.711) --)
  G01 X-070.711 Y0070.711 Z0003.000 F250.0 
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


  (--drill hole #05 at pos (-96.593, 25.882) --)
  G01 X-096.593 Y0025.882 Z0003.000 F250.0 
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


  (--drill hole #06 at pos (-96.593, -25.882) --)
  G01 X-096.593 Y-025.882 Z0003.000 F250.0 
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


  (--drill hole #07 at pos (-70.711, -70.711) --)
  G01 X-070.711 Y-070.711 Z0003.000 F250.0 
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


  (--drill hole #08 at pos (-25.882, -96.593) --)
  G01 X-025.882 Y-096.593 Z0003.000 F250.0 
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


  (--drill hole #09 at pos (25.882, -96.593) --)
  G01 X0025.882 Y-096.593 Z0003.000 F250.0 
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


  (--drill hole #10 at pos (70.711, -70.711) --)
  G01 X0070.711 Y-070.711 Z0003.000 F250.0 
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


  (--drill hole #11 at pos (96.593, -25.882) --)
  G01 X0096.593 Y-025.882 Z0003.000 F250.0 
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
