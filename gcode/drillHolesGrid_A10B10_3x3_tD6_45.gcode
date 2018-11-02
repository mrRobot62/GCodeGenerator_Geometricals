%

(set ContourHoles preamble)
G21 G90 G64 G17 G40 G49
G21

(set Z saftey position)
G00 Z0010.000 F200.0 

(--- START DRILL HOLES ---)
 (--Hole #01 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0000.000 Y0000.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0000.000 Y0000.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #02 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0008.660 Y0005.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0008.660 Y0005.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #03 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0017.321 Y0010.000 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0017.321 Y0010.000 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #04 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X-005.000 Y0018.660 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X-005.000 Y0018.660 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #05 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0003.660 Y0023.660 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0003.660 Y0023.660 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #06 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0012.321 Y0028.660 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0012.321 Y0028.660 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #07 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X-015.000 Y0045.981 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X-015.000 Y0045.981 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #08 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X-006.340 Y0050.981 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X-006.340 Y0050.981 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

 (--Hole #09 at angle 030.0deg --)
    G01 Z0003.000 F120.0 
  G01 X0002.321 Y0055.981 F100.0 
  (-- start loop --)
  (drill)
  G01 Z-000.500 F0120 
  G01 X0002.321 Y0055.981 F100.0 

  G00 Z0003.000 F0200 
  (-- end loop --)

(--- END DRILL HOLES ---)
G01 Z0010.000 F200.0 
G01 X0000.000 Y0000.000 F200.0 
G00 Z10 F100 
M2

%
