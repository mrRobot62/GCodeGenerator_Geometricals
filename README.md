# GCode - Generator - Python - LinuxCNC

With this python collection it is possible to create simple geometrical shapes and generate gcode.
Primary this tool set is used for my LinuxCNC milling machines.

**Tested with Python 2.7
Status October 2018 - under development - currently contourARC is finished **


## History:
| Version | Description |
|---------|----------------------------------------------------|
|0.1 | initial version with contour circel shape unstable version |
|0.2 | save to file implemented |
|0.3 | contourRectange & contourHoles |

## Starting from console
python main.py



# Implement new shapes, pockets, surfaces, ...
To extend functionality of this tool, there are two things to do

## Extend Menu
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

## Implement your new functions
Use `shapeTemplate.py`and make a copy of this file. Rename the copy to a approperiate filename like `contourArc.py`

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
With button "GCode" you can check your generated GCODE **before** you do it on your CNC
