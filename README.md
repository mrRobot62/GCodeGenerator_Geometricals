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
** Step 1: **
Create your widgets for your shape (`def body (self, master)`)
```
...
        row = row + 1
        self.__speed_XY_G02G03 = StringVar()
        self.__speed_Z_G01 = StringVar()
        Label(master, text="Feed (G02/G03 X/Y):").grid(row=row, column=0, sticky=W)
        Label(master, text="Feed (G01 Z):").grid(row=row, column=2, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_XY_G02G03, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_Z_G01, mandatory=False).grid(
            row=row, column=3, sticky=W)

        #------- insert your individual widgets here ---------------------

        #-----------------------------------------------------------------
...
```
** Step 2: ***
Create your individual gcode in `def apply(self)`

```
    def apply(self):
        gc = "%"
        # Preamble
        gc += CR + "(set countour arc preamble)" + CR
        gc += self.__preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        #--------------------------------------------------------------
        #   start individual gcode
        #--------------------------------------------------------------


        #--------------------------------------------------------------
        #   end individual gcode
        #--------------------------------------------------------------
```

### Preparing `geometricals.py`
**Step 1:**
Create a callback methode to call your new shape template (like DialogContourArc)

```
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
```
**Step 2:**
Insert your callback method into menu (like DialogContourArc)

```
# Contour - Arc
self.ContourMenu.add_command(label="Arc", command=self.DialogContourArc)
#--------- Insert arc shapes here ---------------------#

#------------------------------------------------------#

# sub menu Drilling
self.DrillingMenu = Menu(self.FileMenu)
self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)
#--------- Insert drilling shapes here ---------------------#

#------------------------------------------------------#
```



