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

"""

from Tkinter import *
from tkFont import Font
from math import *
import tkMessageBox
import os

from geometric_ContourArc import *

IN_AXIS = os.environ.has_key("AXIS_PROGRESS_BAR")
CR = '\n'

'''
    Geometrical Main-Application

    This Application is only a frame around differnt GCode-Generator classes.

    Via Menu, the GCode-Generator class is called. Every class return the corresponding
    gcode.

    Inside Main-Application this GCode is displayed in a text box and can
    * clipboard
    * file

'''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.geometry("800x610")
        self.sourceFont = Font(family="Courier", size=12)
        self.grid()
        self.gcode_comment = """
%% ---------------- LunaX -----------------------
%% this gcode was generated from geometric.py
%%
%% (C) 2018 by LunaX
"""
        self.gcode_content = StringVar()
        self.gcode_post = StringVar()
        self.gcode_pre = StringVar()

    def init(self, app):
        self.parent = app
        self.createMenu()
        self.createWidgets()
        pass

    def createMenu(self):
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

        # Contour - Arc
        self.ContourMenu.add_command(label="Arc", command=self.DialogContourArc)

        # sub menu Drilling
        self.DrillingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Drilling", menu=self.DrillingMenu)

        # sub menu Pocketing
        self.PocketingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Pocketing", menu=self.PocketingMenu)

        # sub menu Engraving
        self.EngravingMenu = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="Engraving", menu=self.EngravingMenu)

        # Quit
        self.FileMenu.add_command(label="Quit", command=self.quit)

    def createWidgets(self):
        self.EntryFrame = Frame(self, bd=1)
        self.EntryFrame.grid(row=0, column=0)

        self.l01 = Label(self.EntryFrame, text='generated G-Code')
        self.l01.grid(row=0,column=0, columnspan=2, sticky=W+E+N+S)

        self.g_code = Text(self.EntryFrame, width=60, height=40, font=self.sourceFont)
#       self.ScrollBar = Scrollbar(self.parent)
#       self.ScrollBar.config(command=self.g_code.yview)
#        self.g_code.config(yscrollcommand=self.ScrollBar.set)
        self.g_code.grid(row=1, column=0, columnspan=2, rowspan=19, sticky=W+E+N+S)

        self.l02 = Label(self.EntryFrame, text='Pre G-Code')
        self.l02.grid(row=1,column=2)
        self.g_code_pre = Entry(self.EntryFrame, width=30, textvariable=self.gcode_pre)
        self.g_code_pre.grid(row=1, column=3)
        #self.g_code_pre.bind('<FocusOut>', self.PreGCode)

        self.BtnClearButton = Button(self.EntryFrame, text ="Update")
        self.BtnClearButton.grid(row=2,column=2, sticky=W)
        self.BtnClearButton.bind("<Button-1>", self.PreGCode)

        self.l03 = Label(self.EntryFrame, text='Post G-Code')
        self.l03.grid(row=3,column=2)
        self.g_code_post = Entry(self.EntryFrame, width=30, textvariable=self.gcode_post)
        self.g_code_post.grid(row=3, column=3)

        self.BtnClearButton = Button(self.EntryFrame, text ="Update")
        self.BtnClearButton.grid(row=4,column=2, sticky=W)
        self.BtnClearButton.bind("<Button-1>", self.PostGCode)


        #---- general Buttons -----
        btn_row = 20
        self.BtnClearButton = Button(self.EntryFrame, text ="Clear gcode")
        self.BtnClearButton.grid(row=btn_row,column=0, sticky=W)
        self.BtnClearButton.bind("<Button-1>", self.ClearGCode)

        self.BtnCopyClipboard = Button(self.EntryFrame, text ="copy to clipboard")
        self.BtnCopyClipboard.grid(row=btn_row,column=1, sticky=W)
        self.BtnCopyClipboard.bind("<Button-1>", self.CopyClipboard)

        btn_row = btn_row + 1
        self.BtnSaveFile = Button(self.EntryFrame, text ="Save to file")
        self.BtnSaveFile.grid(row=btn_row,column=0, sticky=W)
        self.BtnSaveFile.bind("<Button-1>", self.SaveFile)

        self.BtnSave2Axis = Button(self.EntryFrame, text ="Save to AXIS")
        self.BtnSave2Axis.grid(row=btn_row,column=1, sticky=W)
        self.BtnSave2Axis.bind("<Button-1>", self.Write2Axis)

        self.BtnQuit = Button(self.EntryFrame, text ="Quit", command=self.quit)
        self.BtnQuit.grid(row=btn_row,column=2, sticky=W)

        #----
        self.g_code.insert(END, self.gcode_comment)
        self.g_code.insert(END, CR)
        pass

    def CopyClipboard(self, event):
        self.gcode.clipboard_clear()
        self.gcode.clipboard_append(self.gcode.get())

    def ClearGCode(self, event):
        self.PreGCode()
        pass

    def SaveFile(self, event):
        pass

    def Write2Axis(self, event):
        sys.stdout.write(self.gcode.get())
        self.quit()

    def PreGCode(self, event=''):
        self.g_code.delete(1.0, END)
        self.g_code.insert(END, self.gcode_comment)
        self.g_code.insert(END, '%--------- Pre GCode ---------\n')
        self.g_code.insert(END, self.gcode_pre.get())
        pass

    def PostGCode(self, event=''):
        self.g_code.insert(END, "%--------- Post GCode ---------\n")
        self.g_code.insert(END, self.gcode_post.get())
        pass

    #------ Menu callbacks ----------------
    def DialogContourArc(self):
        #print("call ContourArc")
        d = ClassContourArc(self.parent, "Arc/Circle contours")
        gcode = d.result
        print "GCode: {}".format(gcode)
        if gcode != None:
            self.g_code.insert(END, gcode)

    #------ EXIT --------------------------
    def Quit():
        self.quit()
        pass

#-----------------------------------------------------------

app = Application()
app.init(app)
app.master.title("Geometricals 0.1")
app.mainloop()
