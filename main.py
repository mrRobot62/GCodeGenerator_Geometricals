#!/usr/local/bin/python

"""
    Simple geometrical G-Code Generator
    Version 0.1
    Copyright (C) <2018> <LunaX> alias <Bernd Klein>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    e-mail me any suggestions to "bjt 128 at gmail dot com"
    If you make money using this software
    you must donate $20 USD to a local food bank
    or the food police will get you! Think of others from time to time...

    To make it a menu item in Ubuntu use the Alacarte Menu Editor and add
    the command python YourPathToThisFile/face.py
    make sure you have made the file execuatble by right
    clicking and selecting properties then Permissions and Execute

    To use with LinuxCNC see the instructions at:
    https://github.com/linuxcnc/simple-gcode-generators

    0.1 intial with ARCGEN function
    0.2 file save implemented

"""

from Tkinter import *
from tkFont import Font
from math import *
import tkMessageBox
import os

from contourArc import *
from contourRectangle import *
from contourRoundRectangle import *
from contourHoles import *
from contourMillHolesGrid import *

from pocketRoundRectangle import *
from pocketCircle import *
from pocketRectangle import *

from drillHoles import *
from drillHolesGrid import *

from surfaceRectangle import *
from surfaceCircle import *

#from toolTable import *
IN_AXIS = os.environ.has_key("AXIS_PROGRESS_BAR")
CR = '\n'

VERSION = " (0.12.3)"

'''
    Geometrical Main-Application

    This Application is only a frame around differnt GCode-Generator classes.

    Via Menu, the GCode-Generator class is called. Every class return the corresponding
    gcode.

    Inside Main-Application this GCode is displayed in a text box and can
    * clipboard
    * file

    History
    0.1 initial with ContourArc
    0.2 ContourRectangle
    0.3 contourHoles
    0.4 contourMillHolesGrid

    0.10 surfaceRectangle (base version)
    0.11 surfaceCircle(base version)
    0.12.1 bugfix-release. Fixed issues
            #5, #6, #9, #12a+b,
    0.12.2 bugfix-release. Fixed issues
            #13, #14
    0.12.3 bugfix-release. Fixed issues
            #15, #18 (close Window)
    0.12.4 bugfix-release. Fixed issues
            #10 TooldID, SpindleSpeed, SpindleDir

'''
class GCodeGenerator(Frame):
    def __init__(self, master=None, title=""):
        self.frame = Frame.__init__(self, master)
#        self.master.geometry("800x610")
        self.sourceFont = Font(family="Courier", size=12)
        self.grid()
        pass

    def init(self, app):
        self.app = app
        self.__createMenu()
        pass

    def __createMenu(self):
        # create Menu base
        self.menu = Menu(self)
        # add menu
        self.master.config(menu=self.menu)
        # file menu
        self.FileMenu = Menu(self.menu)
        # add our menu to the base menu
        self.menu.add_cascade(label='File', menu=self.FileMenu)

        # sub menu Contour
        self.ContourMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Contour", menu=self.ContourMenu)

        #--------- Insert contour shapes here ---------------------#
        # Contour - Arc
        self.ContourMenu.add_command(label="Circle or Arc", command=self.DialogContourArc)
        # Contour - Arc
        self.ContourMenu.add_command(label="Rectangle", command=self.DialogContourRec)
        # Contour - Arc
        self.ContourMenu.add_command(label="Rounded rectangle", command=self.DialogContourRoundedRec)
        # Contour - Holes
        self.ContourMenu.add_command(label="Holes on circle", command=self.DialogContourHoles)
        # Contour - Holes on a grid
        self.ContourMenu.add_command(label="Holes on grid", command=self.DialogContourHolesGrid)

        #------------------------------------------------------#

        # sub menu Drilling
        self.DrillingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)
        #--------- Insert drilling shapes here ---------------------#

        self.DrillingMenu.add_command(label="Drill holes", command=self.DrillHoles)
        self.DrillingMenu.add_command(label="Drill holes grid", command=self.DrillHolesGrid)
         #------------------------------------------------------#

        # sub menu Pocketing
        self.PocketingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Pocketing", menu=self.PocketingMenu)
        #--------- Insert pocketing shapes here ---------------------#
        self.PocketingMenu.add_command(label="Mill a circle pocket", command=self.PocketCircle)
        self.PocketingMenu.add_command(label="Mill a round rect pocket", command=self.PocketRoundRectangle)
        self.PocketingMenu.add_command(label="Mill a rectangle pocket", command=self.PocketRectangle)

        #------------------------------------------------------#

        # sub menu Surface
        self.SurfaceMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Surface", menu=self.SurfaceMenu)
        #--------- Insert engraving shapes here ---------------------#
        self.SurfaceMenu.add_command(label="surface milling Rectangle", command=self.SurfaceRectangle)
        self.SurfaceMenu.add_command(label="surface milling Circle", command=self.SurfaceCircle)

        #------------------------------------------------------#
        # sub menu Engraving
        self.EngravingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Engraving", menu=self.EngravingMenu)
        #--------- Insert engraving shapes here ---------------------#

        #------------------------------------------------------#
        #self.FileMenu.add_command(label="Tool table", command=self.ToolTable)

        # Quit
        self.FileMenu.add_command(label="Quit", command=self.quit)

    def closeDialog(self):
        self.myApp.onClose()
        pass

#------ Menu callbacks ----------------
    def DialogContourArc(self):
        self.master.deiconify()
        print "DialogContourArc"
        title = "Contour Arc" + VERSION
        self.myApp = ContourArc(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourRec(self):
        self.master.deiconify()
        print "DialogContourRec"
        title = "Contour Rectangle" + VERSION
        self.myApp = ContourRectangle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass


    def ToolTable(self):
        self.master.deiconify()
        print "Tool table"
        title = "Tool table" + VERSION
        self.myApp = ToolTable(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show(showImage=False,
            showStandardContent=False,
            showStandartButton=False)
        pass

    def DialogContourRoundedRec(self):
        self.master.deiconify()
        print "DialogContourRoundedRec"
        title = "Contour Rounded Rectangle" + VERSION
        self.myApp = DialogContourRoundedRec(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourHoles(self):
        self.master.deiconify()
        print "DialogContourHoles"
        title = "Contour Holes on a circle" + VERSION
        self.myApp = ContourHoles(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourHolesGrid(self):
        self.master.deiconify()
        print "DialogContourHolesGrid"
        title = "Mill holes on a grid" + VERSION
        self.myApp = ContourMillHolesGrid(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def PocketRoundRectangle(self):
        self.master.deiconify()
        print "PocketRoundRectangle"
        title = "Mill round rectangle pocket" + VERSION
        self.myApp = PocketRoundRectangle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def PocketRectangle(self):
        self.master.deiconify()
        print "PocketRectangle"
        title = "Mill rectangle pocket" + VERSION
        self.myApp = PocketRectangle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def PocketCircle(self):
        self.master.deiconify()
        print "PocketCircle"
        title = "Mill pocket circle" + VERSION
        self.myApp = PocketCircle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DrillHoles(self):
        self.master.deiconify()
        print "DrillHoles"
        title = "Drill holes in a circle" + VERSION
        self.myApp = DrillHoles(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DrillHolesGrid(self):
        self.master.deiconify()
        print "DrillHolesGrid"
        title = "Drill holes in a grid" + VERSION
        self.myApp = DrillHolesGrid(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def SurfaceRectangle(self):
        self.master.deiconify()
        print "SurfaceRectangle"
        title = "surface milling a rectangle" + VERSION
        self.myApp = SurfaceRectangle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def SurfaceCircle(self):
        self.master.deiconify()
        print "SurfaceCircle"
        title = "surface milling a spiral" + VERSION
        self.myApp = SurfaceCircle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

#--------- Menu callbacks ---------------------#


def on_closing():
#    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        #print ("Destroy main window ({})".format(app.tk.call('winfo', 'children', '.')))
        #i=0
        app.myApp.destroy()
        app.master.withdraw()
        # widgetList = app.tk.call('winfo', 'children', '.')
        # for widget in widgetList:
        #     print ("Destroy widget #{0:02d} => ({1})".format(i,widget))
        #     widget.destroy()
        #     i += 1
        # app.master.withdraw()


#------------------------------------------------------#

app = GCodeGenerator()
app.init(app)
app.master.title("Geometricals {}".format(VERSION))
app.master.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()

#-----------------------------------------------------------
