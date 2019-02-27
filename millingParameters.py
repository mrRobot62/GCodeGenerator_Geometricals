'''
    this file contain stuff around MillingParameters

    Current tool table is stored as a plain ascii file. File format is
    LinuxCNC tool table format up from version 2.4 and FloatEntry
    (http://wiki.linuxcnc.org/cgi-bin/wiki.pl?MillingParameters)

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
import json

CR = "\n"


class MillingParameters(GeometricalFrame):

    def init(self):
        self.json_fn    = "./millingparameters.json"
        self.col_fmt    = ["{:10}",     "{:4d}",    "{:10}",    "{:05.3f}",     "{:04.1f}",     "{:05.1f}",     "{:04.1f}",     "{:5d}",        "{}"]
        self.colH1      = ["Material",  "ToolID",   "Tool",     "Tool Diameter","Feed rate 1",  "Feed rate 2",  "Infeed rate",  "Spindel-RPM",  "Info"]
        self.colH2      = ["(String)",  "(int)",    "(String)", "(mm)",         "(mm/sec)",     "(mm/min)",     "(mm/min)",     "(rpm)",        "(String)"]
        self.rows = []
        self.__imageNames = []
        self.__json = []
        self.loadJSON()
        self.materialList = self.getAllMaterials()
        self.parameters = self.getMaterialParameterList("Metal")

    #------------------------------------------------------------
    # JSON handling stuff
    #------------------------------------------------------------
    def loadJSON (self):
        print ("load {}".format(self.json_fn))
        with open(self.json_fn, 'r') as f:
            self.__json = json.load(f)

        pass

    def saveJSON(self):
        print ("save {}".format(self.json_fn))
        with open(self.json_fn, 'w') as f:
                json.dump(self.__json, f)
        pass

    def getAllMaterials(self):
        materials = []
        for material in self.__json:
            print ("Material {}".format(material))
            materials.append(material)

        return materials

    def getMaterialParameterList(self, material):
        parameters = self.__json[material]
        print parameters
        return parameters

    #------------------------------------------------------------
    # EntryGrid 
    #------------------------------------------------------------

    

    #------------------------------------------------------------
    # Widget logic
    #------------------------------------------------------------

    def _changeImage(self):
        pass

    def _frmIndividualContent(self):
        self.init()
        row = 0

        #-----------------------------------------------------
        # create a grid frame
        #-----------------------------------------------------
        self.frmTable = EntryGrid(
            self.parentFrame,
            self.colH1,
            self.rows,
            self.col_fmt,
            title="Milling Parameters", 
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
        return True

    def updateEntryGrid(self):
        pass

    def generateGCode(self):
        return  None

    def loadMillingParameters(self):
        pass

    def saveMillingParameters(self):
        pass
