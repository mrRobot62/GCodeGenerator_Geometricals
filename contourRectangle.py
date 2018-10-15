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
class ContourRectangle(GeometricalFrame):

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
        Label(self.frmImage, image=self.photo).grid(
            row=0, column=0, sticky=W+E+N+S, columnspan=2
        )

    #-------------------------------------------------------------
    # her you should insert your own widgets which are important
    # for generating your own GCode
    #-------------------------------------------------------------
    def _frmIndividualContent(self):
        self.init()
        row = 0
        choices = [1,2,3,4,5,6,7,8,9]

        self.__CC = StringVar()
        self.__CC.set(choices[8])
        self._changeImage(self.__CC.get())
        Label(self.frmButtonsIndividualContent, text='Coordinate Center').grid(row=row, column=0, sticky=W)
        OptionMenu(self.frmButtonsIndividualContent,
            self.__CC, *choices, command=self._changeImage).grid(
            row=row, column=1)


        row += 1
        self.__unit = StringVar()
        self.__unit.set("G21")
        Label(self.frmButtonsIndividualContent, text='Unit').grid(row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="mm", variable=self.__unit,
                    value="G21").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="inch", variable=self.__unit,
                    value="G20").grid(row=row, column=2, sticky=W)

        row += 1
        self.__dir = StringVar()
        self.__dir.set("G02")
        Label(self.frmButtonsIndividualContent, text='Contour direction').grid(
            row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="CW (G02)", variable=self.__dir,
                    value="G02").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="CCW (G03)", variable=self.__dir,
                    value=1).grid(row=row, column=2, sticky=W)

        row += 1
        self.__cuttercompensation = StringVar()
        self.__cuttercompensation.set("G40")
        Label(self.frmButtonsIndividualContent, text='Tool movement').grid(row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="on contour", variable=self.__cuttercompensation,
            value="G40").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="left from contour", variable=self.__cuttercompensation,
            value="G41").grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="right from contour", variable=self.__cuttercompensation,
            value="G42").grid(row=row, column=3, sticky=W)

        row += 1
        self.__tooldia = StringVar(value="3.0")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text='Center X (only for 1,2,3,4)').grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text='Center Y (only for 1,2,3,4)').grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerX).grid(row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerY).grid(row=row, column=3, sticky=W)

        row += 1
        self.__heightA = StringVar(value="20.0")
        self.__widthB = StringVar(value="30.0")
        Label(self.frmButtonsIndividualContent, text="Height A").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Width B").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__heightA).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__widthB).grid(row=row, column=3, sticky=W)

        row += 1
        self.__depthtotal = StringVar(value="-0.5")
        self.__depthstep = StringVar(value="-0.5")
        Label(self.frmButtonsIndividualContent, text="Total depth").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="depth cutting per step").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__depthtotal, mandatory=True).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__depthstep, mandatory=True).grid(
            row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G00 = StringVar(value="200.0")
        self.__speed_Z_G00 = StringVar(value="200.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G00 X/Y)").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G00 Z)").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_XY_G00, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_Z_G00, mandatory=False).grid(row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G02G03 = StringVar(value="80.0")
        self.__speed_Z_G01 = StringVar(value="50.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G01 X/Y)").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G01 Z)").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_XY_G02G03, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_Z_G01, mandatory=False).grid(
            row=row, column=3, sticky=W)

        row += 1
        self.__start_Z = StringVar(value="3.0")
        Label(self.frmButtonsIndividualContent, text="Start Z").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__start_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)

        row += 1
        self.__safety_Z = StringVar(value="10.0")
        Label(self.frmButtonsIndividualContent, text="Safety Z").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__safety_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)

        #-----------------------------------------------------
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

#    def show(self):
#        GeometricalFrame.show()
#        self.setBtnStates(state=DISABLED)

    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):
        X = float(0.0)
        Y = float(0.0)
        Z = float(0.0)

        xoffset = float(0.0)
        yoffset = float(0.0)
        a = float(self.__heightA.get())
        b = float(self.__widthB.get())

        gc = ""
        # Preamble
        gc += CR + "(set countour rectangle preamble)" + CR
        gc += self._preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        #
        # even which center point user choosed, we start on
        # center point object - left down (5)

        # mill left down
        if (int(self.__CC.get()) == 1):
            X = float(self.__centerX.get())
            Y = float(self.__centerY.get())
        # mill left upper
        if (int(self.__CC.get()) == 2):
            X = float(self.__centerX.get())
            Y = -float(self.__centerY.get())
        # mill right upper
        if (int(self.__CC.get()) == 3):
            X = -float(self.__centerX.get())
            Y = -float(self.__centerY.get())
        # mill right down
        if (int(self.__CC.get()) == 4):
            X = -float(self.__centerX.get())
            Y = float(self.__centerY.get())

        # object left down - this is our real center point
        if (int(self.__CC.get()) == 5):
            X = float(0.0)
            Y = float(0.0)
        # object left upper
        if (int(self.__CC.get()) == 6):
            X = float(0.0)
            Y = float(0.0) - a
        # object right upper
        if (int(self.__CC.get()) == 7):
            X = float(0.0) - b
            Y = float(0.0) - a
        # object right down
        if (int(self.__CC.get()) == 8):
            X = float(0.0) - b
            Y = float(0.0)
        # object center
        if (int(self.__CC.get()) == 9):
            print "cc 9"
            X += float(0.0) - (b/2.0)
            Y = float(0.0) - (a/2.0)

        # cutter compensation
        ccX = 0.0
        ccY = 0.0
        if (self.__cuttercompensation.get() == "G40"):
            gc += CR + "(-- Cutter compensation --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
        if (self.__cuttercompensation.get() == "G41"):
            gc += CR + "(-- Cutter compensation LEFT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
            ccX = -(float(self.__tooldia) / 2.0)
            ccY = -(float(self.__tooldia) / 2.0)
        if (self.__cuttercompensation.get() == "G42"):
            gc += CR + "(-- Cutter compensation RIGHT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
            ccX = (float(self.__tooldia) / 2.0)
            ccY = (float(self.__tooldia) / 2.0)

        if (self.__dir.get() == "G03"):
            # mill run CCW
            ccX *= -1
            ccY *= -1

        X += ccX
        Y += ccY

        #
        # generate as many shape steps are needed until depthtotal is reached
        # cut an Arc
        step = float(self.__depthstep.get())
        depth = float(self.__depthtotal.get())
        z = step
        loop = ""
        gc += CR + "(------- start shape -------------)" + CR
        gc += "(-- A {0:06.3f}, B {1:06.3f}, Depth {2:06.3f}, Step {3:06.3f} --){4}".format(
            float(a),
            float(b),
            depth,
            step,
            CR
        )
        gc += "(-- X {0:06.3f}, Y {1:06.3f} --) {2}".format(
            float(X),
            float(Y),
            CR
        )
        # start with shape
        gc += CR + "(move Z-axis to start postion near surface)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__start_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        # set start postion X/Y
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            float(X),
            float(Y),
            float(self.__speed_XY_G00.get()),
            CR)


        #----------------------------------------------------------------------
        # This loop asume, that you try to mill into your object.
        # if not needed for your shape, remove this part and rewrite
        #----------------------------------------------------------------------
        #
        gc += CR + "(-- loop --)" + CR
        # start with shape

        # set start postion X/Y
        while (abs(z) < abs(depth)):
            # set next Z depth
            if ((abs(depth) - abs(z)) < abs(step)):
                # this happens, if a small amount is the rest
                z -= (abs(depth) - abs(z))
                print "rest Z: {}".format(z)
            else:
                z -= abs(step)
                print "new Z: {}".format(z)

            #
            # start with this start position
            loop += self.__createGCodeRect(X,Y,Z,a,b)

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
        #print gc
        return  gc

    def __createGCodeRect(self, x,y,z,a,b):
        gc = ""
        gc += CR + "(set new Z {0:05.2f} position)".format(z) + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(z),
            float(self.__speed_Z_G00.get()), CR)

        # go to left up
        gc += "G01 X{0:08.3f} Y{1:08.3f} Z{2:08.3f} F{3:05.1f} {4}".format(
                float(x),
                float(y + a),
                float(z),
                float(self.__speed_XY_G02G03.get()),
                CR)
        # go right up
        gc += "G01 X{0:08.3f} Y{1:08.3f} Z{2:08.3f} F{3:05.1f} {4}".format(
                float(x + b),
                float(y + a),
                float(z),
                float(self.__speed_XY_G02G03.get()),
                CR)
        # go right down
        gc += "G01 X{0:08.3f} Y{1:08.3f} Z{2:08.3f} F{3:05.1f} {4}".format(
                float(x),
                float(y-b),
                float(z),
                float(self.__speed_XY_G02G03.get()),
                CR)
        # back to start (left down)
        gc += "G01 X{0:08.3f} Y{1:08.3f} Z{2:08.3f} F{3:05.1f} {4}".format(
                float(x),
                float(y),
                float(z),
                float(self.__speed_XY_G02G03.get()),
                CR)
        return gc
