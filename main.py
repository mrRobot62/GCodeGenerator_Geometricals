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
from contourHoles import *
from contourMillHolesGrid import *

IN_AXIS = os.environ.has_key("AXIS_PROGRESS_BAR")
CR = '\n'

VERSION = "0.4 (2018-10-18)"

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
        # Contour - Holes
        self.ContourMenu.add_command(label="Holes on circle", command=self.DialogContourHoles)
        # Contour - Holes on a grid
        self.ContourMenu.add_command(label="Holes on grid", command=self.DialogContourHolesGrid)

        #------------------------------------------------------#

        # sub menu Drilling
        self.DrillingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)
        #--------- Insert drilling shapes here ---------------------#

        #------------------------------------------------------#

        # sub menu Pocketing
        self.PocketingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Pocketing", menu=self.PocketingMenu)
        #--------- Insert pocketing shapes here ---------------------#

        #------------------------------------------------------#

        # sub menu Engraving
        self.EngravingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Engraving", menu=self.EngravingMenu)
        #--------- Insert engraving shapes here ---------------------#

        #------------------------------------------------------#

        # Quit
        self.FileMenu.add_command(label="Quit", command=self.quit)



#------ Menu callbacks ----------------
    def DialogContourArc(self):
        print "DialogContourArc"
        title = "Contour Arc"
        self.myApp = ContourArc(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourRec(self):
        print "DialogContourRec"
        title = "Contour Rectangle"
        self.myApp = ContourRectangle(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourHoles(self):
        print "DialogContourHoles"
        title = "Contour Holes on a circle"
        self.myApp = ContourHoles(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass

    def DialogContourHolesGrid(self):
        print "DialogContourHolesGrid"
        title = "Mill holes on a grid"
        self.myApp = ContourMillHolesGrid(self.app, self.master, self.frame, title)
        self.myApp.init()
        self.myApp.show()
        pass


#--------- Menu callbacks ---------------------#

#------------------------------------------------------#

app = GCodeGenerator()
app.init(app)
app.master.title("Geometricals {}".format(VERSION))
app.mainloop()

#-----------------------------------------------------------
