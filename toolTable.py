'''
    this file contain stuff around toolTable using

    Current tool table ist stored as a plain ascii file. File format is
    LinuxCNC tool table format up from version 2.4 and FloatEntry
    (http://wiki.linuxcnc.org/cgi-bin/wiki.pl?ToolTable)

    File is imported and converted into a json structure.


'''

from tkSimpleDialog import *
from Tkinter import *
from tkFont import Font
from math import *
import PIL.Image
import PIL.ImageTk
from GeometricalFrame import *

import tkMessageBox
import os

CR = "\n"


class ToolTable(GeometricalFrame):

    def init(self):
        self.col_fmt = ["T{04d}","P{02d}","X{08.3f}","Y{08.3f}","Z{08.3f}",";{} End Mill"]
        self.cols = ["Tool","Pocket","XOffset","YOffset","ZOffset","Remark"]
        self.rows = []
        self.__imageNames = [
            # left down
            "./img/contour/circle-pic1_1.jpg",
            # left upper
            "./img/contour/circle-pic1_2.jpg",
            # right upper
            "./img/contour/circle-pic1_3.jpg",
            # right down
            "./img/contour/circle-pic1_4.jpg",
            # center
            "./img/contour/circle-pic1_5.jpg"
        ]

    def _changeImage(self):
        print len(self.__imageNames)
        p = self.__imageNames[int(self.__CC.get())-1]
        self.img = PIL.Image.open(p)
        self.photo = PIL.ImageTk.PhotoImage(self.img)
        Label(self.frmImage, image=self.photo).grid(
            row=0, column=0, sticky=W+E+N+S, columnspan=2
        )

    def _frmIndividualContent(self):
        self.init()
        row = 0

        self.__filename = StringVar(value="")
        Label(self.frmButtonsIndividualContent, text="Path & Filename").grid(
            row=row, column=0, sticky=W)
        w1a = StringEntry(self.frmButtonsIndividualContent, width=25,
            mandatory=True, textvariable=self.__filename,
            background="Red")
        w1a.grid(row=row, column=1, sticky=W)
        ToolTip(w1a,text= '''Please choose path & filename''')

        row += 1
        self.__toolid = StringVar(value="0")
        self.__pocketid = StringVar(value="0")
        Label(self.frmButtonsIndividualContent, text="ToolID").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="PocketID").grid(
            row=row, column=2, sticky=W)
        w2a = IntEntry(self.frmButtonsIndividualContent, width=5, mandatory=True,
            textvariable=self.__toolid)
        w2a.grid(row=row, column=1, sticky=W)
        w2b = IntEntry(self.frmButtonsIndividualContent, width=5, mandatory=False,
            textvariable=self.__pocketid)
        w2b.grid(row=row, column=3, sticky=W)
        ToolTip(w2a,text='''Please define tool number''')
        ToolTip(w2b,text='''Please define pocket number''')

        row += 1
        self.__xoffset = StringVar(value="0.0")
        self.__yoffset = StringVar(value="0.0")
        self.__zoffset = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text="XOffset").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="YOffset").grid(
            row=row, column=2, sticky=W)
        Label(self.frmButtonsIndividualContent, text="ZOffset").grid(
            row=row, column=4, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__xoffset).grid(row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__yoffset).grid(row=row, column=3, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__zoffset).grid(row=row, column=5, sticky=W)

        row += 1
        self.__tooldiameter = StringVar(value="")
        self.__toollength = StringVar(value="")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Tool length").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__tooldiameter, mandatory=True,background="Red").grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__toollength, mandatory=False).grid(
            row=row, column=3, sticky=W)

        row += 1
        self.__remark = StringVar(value="")
        Label(self.frmButtonsIndividualContent, text="Remark").grid(
            row=row, column=0, sticky=W)
        StringEntry(self.frmButtonsIndividualContent, width=25,
            textvariable=self.__remark, mandatory=False).grid(
            row=row, column=1, sticky=W)

        #-----------------------------------------------------
        # create a grid frame
        #-----------------------------------------------------
        self.frmTable = EntryGrid(self.parentFrame,
            colList = self.cols,
            rowList = self.rows,
            colFmt = self.col_fmt,
            state="DISABLED"
        )
        self.frmTable.pack(expand=True, fill=BOTH)

        #-----------------------------------------------------
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)


        pass

    def __validation(self, nV, **kv):
        # nothing
        return True

    def userInputValidation(self):
        if (self.__tooldiameter.get() <= 0.0 or
            self.__tooldiameter.get() > 25.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Diameter should be in range > 0.0 and <= 25.0")
            return False

        if (float(self.__toollength.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tool length should be greather than 0.0")
            return False

        if (len(self.__filename) == 0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="File name can't be empty")
            return False

        if (int(self.__toolid.get()) <= 0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="ToolID should be greater than 0")
            return False

        if (int(self.__pocketid.get()) <= 0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="PocketID should be greater than 0")
            return False

        if (float(self.__xoffset.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="X Offset should be greater than 0.0")
            return False

        if (float(self.__yoffset.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Y Offset should be greater than 0.0")
            return False

        if (float(self.__zoffset.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Z Offset should be greater than 0.0")
            return False


        return True

    def updateEntryGrid(self):
        pass

    def generateGCode(self):
        return  None

    def loadToolTable(self):
        pass

    def saveToolTable(self):
        pass
