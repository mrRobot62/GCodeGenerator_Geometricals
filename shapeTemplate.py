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


#----------------------------------------------------------------------------
#
# This class define your GCode generator
#
# It is a subclass from GeometricalFrame and provide a couple of functionalities
# like an image frame, a standard input entries frame, your "own" entries Frame
# and standard Buttons
#
# Copy this file into your your own file. Typical filenames are <kind shape>
# like ContourArc or ContourRect or PocketArc, ...
#
#
#
#----------------------------------------------------------------------------
class shapeTemplate(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        self.__imageNames = [
            # left down
            "./img/contour/rectangle-pic1_1.jpg",
            # left upper
            "./img/contour/rectangle-pic1_2.jpg",
            # right upper
            "./img/contour/rectangle-pic1_3.jpg",
            # right down
            "./img/contour/rectangle-pic1_4.jpg",
            # center
            "./img/contour/rectangle-pic1_5.jpg"
        ]

    #-------------------------------------------------------------
    # change image, if an other center point was used
    #-------------------------------------------------------------
    def _changeImage(self, value):
        print len(self.__imageNames)
        i = int(value) - 1
        if (i >= 5): i = 4

        p = self.__imageNames[i]
        self.img = PIL.Image.open(p)
        self.photo = PIL.ImageTk.PhotoImage(self.img)
        Label(
            self.frmImage, image=self.photo).grid(
                row=0, column=0, sticky=W + E + N + S, columnspan=2)

    #-------------------------------------------------------------
    # her you should insert your own widgets which are important
    # for generating your own GCode
    #-------------------------------------------------------------
    def _frmIndividualContent(self):
        self.init()
        row = 0
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        #------------------------------------------------------------------
        # Standard widgets for every classes
        #------------------------------------------------------------------

        self.__CC = StringVar()
        self.__CC.set(choices[8])
        self._changeImage(self.__CC.get())
        Label(
            self.frmButtonsIndividualContent, text='Coordinate Center').grid(
                row=row, column=0, sticky=W)
        OptionMenu(
            self.frmButtonsIndividualContent,
            self.__CC,
            *choices,
            command=self._changeImage).grid(
                row=row, column=1)

        row += 1
        self.__unit = StringVar()
        self.__unit.set("G21")
        Label(
            self.frmButtonsIndividualContent, text='Unit').grid(
                row=row, column=0, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="mm",
            variable=self.__unit,
            value="G21").grid(
                row=row, column=1, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="inch",
            variable=self.__unit,
            value="G20").grid(
                row=row, column=2, sticky=W)

        row += 1
        self.__dir = StringVar()
        self.__dir.set("G02")
        Label(
            self.frmButtonsIndividualContent, text='Contour direction').grid(
                row=row, column=0, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="CW (G02)",
            variable=self.__dir,
            value="G02").grid(
                row=row, column=1, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="CCW (G03)",
            variable=self.__dir,
            value="G03").grid(
                row=row, column=2, sticky=W)

        row += 1
        self.__cuttercompensation = StringVar()
        self.__cuttercompensation.set("G42")
        Label(
            self.frmButtonsIndividualContent, text='Tool movement').grid(
                row=row, column=0, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="on contour",
            variable=self.__cuttercompensation,
            value="G40").grid(
                row=row, column=1, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="left from contour",
            variable=self.__cuttercompensation,
            value="G41").grid(
                row=row, column=2, sticky=W)
        ttk.Radiobutton(
            self.frmButtonsIndividualContent,
            text="right from contour",
            variable=self.__cuttercompensation,
            value="G42").grid(
                row=row, column=3, sticky=W)

        row += 1
        self.tooldia = StringVar(value="3.0")
        #vcmd = (self.frmButtonsIndividualContent.register(self._updateAngle), '%s', '%S')

        Label(
            self.frmButtonsIndividualContent, text="Tool diameter").grid(
                row=row, column=0, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            mandatory=False,
            textvariable=self.tooldia).grid(
                row=row, column=1, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(
            self.frmButtonsIndividualContent, text='Center X').grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent, text="Center Y").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            mandatory=True,
            textvariable=self.__centerX).grid(
                row=row, column=1, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            mandatory=True,
            textvariable=self.__centerY).grid(
                row=row, column=3, sticky=W)

        #------------------------------------------------------------------
        # include your specific widgets from here
        #------------------------------------------------------------------

        #------------------------------------------------------------------
        # Standard widgets for every classes
        #------------------------------------------------------------------

        row += 1
        self.__depthtotal = StringVar(value="-0.5")
        self.__depthstep = StringVar(value="-0.5")
        Label(
            self.frmButtonsIndividualContent, text="Total depth").grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent,
            text="depth cutting per step").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__depthtotal,
            mandatory=True).grid(
                row=row, column=1, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__depthstep,
            mandatory=True).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G00 = StringVar(value=self._standardGCodeSeq[
            "TRAVEL_SPEEDXYZ"][0])
        self.__speed_Z_G00 = StringVar(value=self._standardGCodeSeq[
            "TRAVEL_SPEEDXYZ"][2])
        Label(
            self.frmButtonsIndividualContent, text="Feed (G00 X/Y)").grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent, text="Feed (G00 Z)").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__speed_XY_G00,
            mandatory=False).grid(
                row=row, column=1, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__speed_Z_G00,
            mandatory=False).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.speed_XY_G02G03 = StringVar(value="100.0")
        self.speed_Z_G01 = StringVar(value="80.0")
        Label(
            self.frmButtonsIndividualContent, text="Feed (G02/G03 X/Y)").grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent, text="Feed (G01 Z)").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.speed_XY_G02G03,
            mandatory=False).grid(
                row=row, column=1, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.speed_Z_G01,
            mandatory=False).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__start_Z = StringVar(value=self._standardGCodeSeq["ZAXIS"][0])
        Label(
            self.frmButtonsIndividualContent, text="Start Z").grid(
                row=row, column=0, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            textvariable=self.__start_Z,
            mandatory=False).grid(
                row=row, column=1, sticky=W)

        #row += 1
        self.__safety_Z = StringVar(value=self._standardGCodeSeq["ZAXIS"][1])
        Label(
            self.frmButtonsIndividualContent, text="Safety Z:").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            textvariable=self.__safety_Z,
            mandatory=False).grid(
                row=row, column=3, sticky=W)

        #-----------------------------------------------------
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):
        #------------------------------------------------------------------
        # Standard gcode generation
        #------------------------------------------------------------------
        gc = ""
        # Preamble
        gc += CR + "(set contour arc preamble)" + CR
        gc += self._preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()), float(self.__speed_Z_G00.get()), CR)

        #------------------------------------------------------------------
        # we assume, that we start at center point of centet point (5)
        # To do this, we calculate all values to this point
        #------------------------------------------------------------------
        cPoint = (0.0, 0.0)
        if (int(self.__CC.get()) == 1):
            # down left to CP
            cPoint = (float(self.__centerX.get()), float(self.__centerY.get()))
        if (int(self.__CC.get()) == 2):
            # upper left to CP
            cPoint = (float(self.__centerX.get()),
                      -float(self.__centerY.get()))
        if (int(self.__CC.get()) == 3):
            # upper right to CP
            cPoint = (-float(self.__centerX.get()),
                      -float(self.__centerY.get()))
        if (int(self.__CC.get()) == 4):
            # down right to CP
            cPoint = (-float(self.__centerX.get()),
                      float(self.__centerY.get()))

        #------------------------------------------------------------------
        # cutter __cuttercompensation
        # depending on your shape, you have to reimplement below Code
        #
        # e.G. if you mill a shape like an rectangle, triangle, ... you
        # have to use X/Y for cutter compensation
        #------------------------------------------------------------------
        # cutter compensation
        if (self.__cuttercompensation.get() == "G40"):
            gc += CR + "(-- Cutter compensation --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(), CR)
        if (self.__cuttercompensation.get() == "G41"):
            gc += CR + "(-- Cutter compensation LEFT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(), CR)
            X -= (float(self.tooldia) / 2.0)
        if (self.__cuttercompensation.get() == "G41"):
            gc += CR + "(-- Cutter compensation RIGHT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(), CR)
            X += (float(self.tooldia) / 2.0)

        # set start postion X/Y
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            float(X), float(Y), float(self.__speed_XY_G00.get()), CR)

        # start with shape
        gc += CR + "(move Z-axis to start postion near surface)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__start_Z.get()), float(self.__speed_Z_G00.get()), CR)
        #
        # generate as many shape steps are needed until depthtotal is reached
        # cut an Arc
        step = float(self.__depthstep.get())
        depth = float(self.__depthtotal.get())
        z = 0.0
        loop = ""
        gc += CR + "(------- start shape -------------)" + CR
        gc += "(-- Dia {0:06.3f}, Depth {1:06.3f}, Step Z {2:06.3f} --){3}".format(
            float(self.__dia.get()), depth, step, CR)
        gc += "(-- X {0:06.3f}, Y {1:06.3f} --) {2}".format(
            float(X), float(Y), CR)
        #----------------------------------------------------------------------
        # This loop assume, that you try to mill into your object.
        # if not needed for your shape, remove this part and rewrite
        #----------------------------------------------------------------------
        #
        gc += CR + "(-- loop --)" + CR
        while (abs(z) < abs(depth)):
            # set next Z depth
            if ((abs(depth) - abs(z)) < abs(step)):
                # this happens, if a small amount is the rest
                z -= (abs(depth) - abs(z))
                print "rest Z: {}".format(z)
            else:
                z -= abs(step)
                print "new Z: {}".format(z)

            loop += CR + "(set new Z {0:05.2f} position)".format(z) + CR
            loop += "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
                float(z), float(self.speed_Z_G01.get()), CR)
            # set direction G02/G03
            #
            loop += self.__dir.get()

            #---------------------------------------------------
            # typical position for your own Gcode
            # indiviual GCode - START
            #
            # maybe due to your implementation, you have to recreate
            # this complete gcode generation method
            #
            #---------------------------------------------------

            #---------------------------------------------------
            # indiviual GCode - END
            #---------------------------------------------------
            #
            # for saftey issues.
            if (abs(step) == 0.0):
                break

        gc += loop
        #----------------------------
        gc += "(----------------------------------)" + CR
        gc += self._postamble.get() + CR
        gc += CR
        print gc
        return gc

    def validate(self):
        # override in your child class
        #
        # useful to validate user input from widgets
        # return False if an error occured
        # return True if everything is ok

        pass
