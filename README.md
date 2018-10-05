# GCode - Generator

With this python collection it is possible to create simple geometrical shapes and generate gcode.
Primary this tool set is used for my LinuxCNC milling machine.

## History:
Version     Content
0.1         initial version with contour circel shape




## Implementing new shapes
Menu is prepared to handle different shapes. The only thing is to implement the corresponding shape python file and include this new file into the menu system.

Use `geometrical_ContourArc.py` as a starting point for your new shapes

### Create new shape file `geometrical_XXXXXX.py`

### Preparing `geometricals.py`
**Step 1:**
Create a callback methode to call your new shape template (like DialogContourArc)

`
#------ Menu callbacks ----------------
def DialogContourArc(self):
    #print("call ContourArc")
    d = ClassContourArc(self.parent, "Arc/Circle contours")
    gcode = d.result
    print "GCode: {}".format(gcode)
    if gcode != None:
        self.g_code.insert(END, gcode)

#--------- Menu callbacks ---------------------#

#------------------------------------------------------#
`
**Step 2:**
Insert your callback method into menu (like DialogContourArc)

`
# Contour - Arc
self.ContourMenu.add_command(label="Arc", command=self.DialogContourArc)
#--------- Insert arc shapes here ---------------------#

#------------------------------------------------------#

# sub menu Drilling
self.DrillingMenu = Menu(self.FileMenu)
self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)
#--------- Insert drilling shapes here ---------------------#

#------------------------------------------------------#
`




