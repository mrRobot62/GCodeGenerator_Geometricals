%

(set preamble)
G21 G90 G64 G17 G40 G49
G21

(set Z saftey position)
G00 Z0010.000 F200.0 

(set center position)
G00 X0000.000 Y0000.000 F200.0 

(------- start shape -------------)

(move Z-axis to start postion near surface)
G00 Z0003.000 Y-003.000 F200.0 

(-- START DEPTH Loop --)
  (-- START Track Loop  --)

  (-- next depth z -001.000 --)
  G01 Z-001.000 
  G01 X0000.000 Y-003.000
  G02 X-013.000 Y0010.000 I0000.000 J0013.000
  G01 X-013.000 Y0060.000
  G02 X0000.000 Y0073.000 I0013.000 J0000.000
  G01 X0080.000 Y0073.000
  G02 X0093.000 Y0060.000 I0000.000 J-013.000
  G01 X0093.000 Y0010.000
  G02 X0080.000 Y-003.000 I-013.000 J0000.000
  G01 X0000.000 Y-003.000
  (-- END Track Loop  --)(-- END DEPTH loop --)
G00 Z10 F100 
M2

%
