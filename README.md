# GCode - Generator - Python - LinuxCNC

With this python collection it is possible to create simple geometrical shapes and generate gcode.
You can use this tool set to include it into LinuxCNC AXIS.

**Tested with Python 2.7
Status October 2018 - under development **


## History:
| Version | Description |
|---------|----------------------------------------------------|
|0.1 | initial version with contour circel shape unstable version |
|0.2 | save to file implemented |
|0.3 | new contourRectange & contourHoles |
|0.4 | new contourMillHolesGrid. Milling holes on a grid |
|0.5 | new pocketRoundRectangle |
|0.6 | new contourRoundRectangle |
|0.7 | new pocketCircle |
|0.8 | new pocketRectangle |
|0.9 | new drill holes on a grid |
|0.10 | new smooth a rectangle surface in parallel lines |
|0.11 | new smooth a round surface in a spiral |
|0.12.1 | bugfix release #5, #6, #9, #12a+b |
|0.12.2 | bugfix #13, #14 |
|0.12.3 | bugfix #15, #18(close window, VersionNumber|



## Example screenshot (more details inside WIKI)
![](https://github.com/mrRobot62/GCodeGenerator_Geometricals/blob/master/img/screenshots/screen_cCircle.png)


## Starting from console
python main.py



# You want to implement new shapes, pockets, surfaces, ... ?
To extend functionality of this tool, there are three things to do

## (1) Extend Menu
To include your new functionality you have to extend the menu.
Open `main.py` and include your stuff here:


```
<snip>
# sub menu Contour
self.ContourMenu = Menu(self.FileMenu)
self.FileMenu.add_cascade(label="Contour", menu=self.ContourMenu)

# Contour - Arc
self.ContourMenu.add_command(label="Arc", command=self.DialogContourArc)
#--------- Insert arc shapes here ---------------------#

#------------------------------------------------------#

# sub menu Drilling
self.DrillingMenu = Menu(self.FileMenu)
self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)
#--------- Insert drilling shapes here ---------------------#

#------------------------------------------------------#
<snap>
```

Implement a callback function like this:

```
<snip>
#------ Menu callbacks ----------------
    def DialogContourArc(self):
        print "DialogContourArc"
        title = "Contour Arc"
        self.myApp = ContourArc(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass
#--------- Menu callbacks ---------------------#

#------------------------------------------------------#
<snap>
```

Do not forget to import your new python module like This `from contourArc import *` at beginning of `main.py`

## (2) Implement your new functions
Use `shapeTemplate.py`and make a copy of this file if you like to start more or less from scratch ;-). Alternative make a copy of an existing shape/pocket/... and rename it. Than start with point 1. 

Rename the copy to a approperiate filename like `pocketEveryShapeIKnow.py`

For more complex implementations, take a look into pocketXXXXX.py implementations.

Start with implementing of your code.

1. Change classname
2. Insert/copy your images into `img`folder
3. Insert path & filename in method `def init`
4. Insert your widgets in `def _frmIndividualContent(self)`
5. Insert your gcode generator functionality in `def generateGCode(self):`

**Testing:**
start main.py, if implemenation in menu.py was correct, you should see, your new
function inside menu.

Use your new function. A new window appears. Check your functionality.
With button "GCode" you can check your generated GCODE **before** you do it on your CNC. Use a GCode-Simulator like NCViewer or CAMotics to visualize and simulate your generated gcode.

If everything is ok, **than** start gcode on your CNC

## (3) give our community a chance to participate on your new implementation
upload you implementation to this github repository.
**THANKS**

