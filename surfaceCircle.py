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
class SurfaceCircle(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        self.__imageNames = [
            # left down
            "./img/surface/spiral_circle_001.png"
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
        #choices = [1,2,3]
        choices = [1]

        self.__CC = StringVar()
        self.__CC.set(choices[0])
        self._changeImage(self.__CC.get())
        Label(self.frmButtonsIndividualContent, text='Coordinate Center').grid(row=row, column=0, sticky=W)
        OptionMenu(self.frmButtonsIndividualContent,
            self.__CC, *choices, command=self._changeImage).grid(
            row=row, column=1)


        #row += 1
        self.__unit = StringVar()
        self.__unit.set("G21")
        Label(self.frmButtonsIndividualContent, text='Unit').grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="mm", variable=self.__unit,
                    value="G21").grid(row=row, column=3, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="inch", variable=self.__unit,
                    value="G20").grid(row=row, column=4, sticky=W)

        row += 1
        self.__dir = StringVar()
        self.__dir.set("G02")
        Label(self.frmButtonsIndividualContent, text='Contour direction').grid(
            row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="CW (G02)", variable=self.__dir,
                    value="G02").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="CCW (G03)", variable=self.__dir,
                    value="G03").grid(row=row, column=2, sticky=W)

        row += 1
        self.__tooldia = StringVar(value="12.0")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)

        # #row += 1
        # self.__radius = StringVar(value="10.0")
        # Label(self.frmButtonsIndividualContent, text="Edge radius (R)").grid(
        #     row=row, column=2, sticky=W)
        # FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
        #     textvariable=self.__radius).grid(row=row, column=3, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text='Center X').grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text='Center Y').grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerX).grid(row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerY).grid(row=row, column=3, sticky=W)

        row += 1
        self.__radius = StringVar(value="50.0")
        Label(self.frmButtonsIndividualContent, text="work piece radius").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__radius).grid(
            row=row, column=1, sticky=W)

        #
        # stepover from row to row
        #row += 1
        self.__stepover = StringVar(value="50")
        Label(self.frmButtonsIndividualContent, text="Stepover tooldia %").grid(
            row=row, column=2, sticky=W)
        w7 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__stepover, mandatory=False)
        w7.grid(
            row=row, column=3, sticky=W)
        ToolTip(w7,text=
        '''This percentage is the overlap from row to row based on tool diameter. Normally the value should be between 30-90%''')

        self.__overshot = StringVar(value="110")
        Label(self.frmButtonsIndividualContent, text="Overshot %").grid(
            row=row, column=4, sticky=W)
        w7a = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__overshot, mandatory=False)
        w7a.grid(
            row=row, column=5, sticky=W)
        ToolTip(w7a,
        text='''This percentage is an overshot for used tool on work piece edges. Normally the value should be between 0-150%. Values >= 100 move tool completely outside from work piece''')


        row += 1
        self.__depthtotal = StringVar(value="-1.0")
        self.__depthstep = StringVar(value="-0.2")
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
        Label(self.frmButtonsIndividualContent, text="Start Z").grid(
            row=row, column=0, sticky=W)
        w98 = FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__start_Z, mandatory=False)
        w98.grid(
            row=row, column=1, sticky=W)
        ToolTip(w98, text="move the z-axis briefly over the surface to this value")

        #row += 1
        self.__safety_Z = StringVar(value="10.0")
        Label(self.frmButtonsIndividualContent, text="Safety Z").grid(
            row=row, column=2, sticky=W)
        w99 = FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__safety_Z, mandatory=False)
        w99.grid(
            row=row, column=3, sticky=W)
        ToolTip(w99, text="move Z to this value if finished")

        #-----------------------------------------------------
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    def userInputValidation(self):
        '''
        this class is used to validate necessary user input fields
        '''
        print ("userInputValidation")
        radius = float(self.__radius.get())
        toolDia = float(self.__tooldia.get())
        stepover = float(self.__stepover.get())
        overshot = float(self.__overshot.get())

        if (radius <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="outer radius should be greater 0.0")
            return False

        if (radius <= toolDia):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="radius can't be less than tool diameter")
            return False

        if (toolDia <= 0.0 or toolDia > radius):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tool diamater should be greater than 0.0 and less than radius")
            return False

        if (stepover < 30 or stepover > 90):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Stepover should be in range 30-90%")
            return False

        if (stepover < 0.0 or stepover > 150.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Overshot should be in range 0-150%")
            return False

        if (overshot < 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="overshot should be greater or equal 0.0")
            return True


        if (abs(float(self.__depthtotal.get())) < abs(float(self.__depthstep.get()))):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Total depth should be deeper or equal depth step")
            return False

        if (float(self.__start_Z.get()) <= 0.0 or float(self.__safety_Z.get())<= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Z parameter values should be greater than 0.0")
            return False

        if (float(self.__tooldia.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tooldiamter should greater than 0.0")
            return False

        return True


    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):
        '''
        for a pocket in an rounded rectangle, even what user set as reference point, we
        recalculate it to inner contour and start with milling on outer line
        of this contour until we touch outer line contour
        '''
        cPoint = (float(self.__centerX.get()),
                  float(self.__centerY.get()))
        radius = float(self.__radius.get())

        toolDia = float(self.__tooldia.get())

        stepover = float(self.__stepover.get())
        overshot = float(self.__overshot.get())

        zPos = {
            "safetyZ" : float(self.__safety_Z.get()),
            "startZ" : float(self.__start_Z.get())
        }

        depth = (
            float(self.__depthtotal.get()),
            float(self.__depthstep.get()),
        )

        dir = self.__dir.get()

        feeds = {
            "XYG0" : float(self.__speed_XY_G00.get()),
            "XYGn" : float(self.__speed_XY_G02G03.get()),
            "ZG0" : float(self.__speed_Z_G00.get()),
            "ZGn" : float(self.__speed_Z_G01.get())
        }
        gc = ""
        # Preamble
        gc += CR + "(set preamble)" + CR
        gc += self._preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            zPos["safetyZ"], feeds["ZG0"],CR)

        #
        # even which center point user choosed, we start on
        # center point object - left down (5)

        # set start postion X/Y
        gc += CR + "(set center position)" + CR
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            cPoint[0],
            cPoint[1],
            feeds["XYG0"],
            CR)
        #
        # generate as many shape steps are needed until depthtotal is reached
        # cut an Arc
        step = float(self.__depthstep.get())
#        depth = float(self.__depthtotal.get())
        z = step
        loop = ""
        gc += CR + "(------- start shape -------------)" + CR

        # start with shape
        gc += CR + "(move Z-axis to start postion near surface)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            zPos["startZ"],
            feeds["ZG0"],
            CR)
        spaces = "".ljust(2)
        #----------------------------------------------------------------------
        # This loop assume, that you try to mill into your object.
        # if not needed for your shape, remove this part and rewrite
        #----------------------------------------------------------------------
        #

        pocketMillTracks = []
        x = 1
        finished = False

        #
        # a gcode spiral on the same plane is a sequence of several arc combined together.
        # every arc radius increase as long as outer radius is reached

        numberOfDepthSteps, restDepth = self.getDepthSteps(depth[0], depth[1])


        print ("cPointX {}, r {}, depthSteps {}, restDepth {}, stepover {}, overshot {}".format(
            cPoint[0], radius, numberOfDepthSteps, restDepth, overshot,
            overshot))
        #
        # depth control
        i = 1
        for d in range (numberOfDepthSteps):
            gc += self.__getGCodeOnTrack(cPoint, feeds, dir,
                        i, z, radius, toolDia, stepover,
                        overshot)
            i += 1
            pass
        #
        # last depth position
        gc += self.__getGCodeOnTrack(cPoint, feeds, dir,
                    numberOfDepthSteps+1, restDepth,
                    radius, toolDia, stepover, overshot)
        gc += "(-- END --)" + CR
        gc += self.getGCode_Homeing(
            x=cPoint[0],
            y=cPoint[1],
            z=zPos["safetyZ"])
        gc += self._postamble.get() + CR
        gc += CR
        return  gc

    def __getGCodeOnTrack(self, cPoint, feeds, dir, dSteps, z,
        radius, toolDia, stepover=80, overshot=0.0):
        '''
        create a gcode sequence for a plane spiral based on given parameters.
        Parameters:
        cPoint    center of spiral
        feeds     speed for x/Y & Z
        dir       turn direction G02 or G03
        dSteps    number of steps for the depth
        z         value for z-axis
        radius    outer radius for spiral
        toolDia   tool diameter
        stepover  overlapping in percent of tool diameter : default 80.0%
        Overshot  increade radius for this value : default 0.0

        '''
        indent = "".ljust(2)
        gc = "(-- Step #{0:03d} Z{1:08.3f} --) {2}".format(
             dSteps, z, CR)
        #
        # calculate stepover and overshot from percentage
        s = round(toolDia - (float(toolDia * stepover) / 100), 1)
        if overshot >= 100:
            o = round((float(toolDia  * overshot) / 100), 1) - (toolDia / 2.0)
        else:
            o = round((float(toolDia * overshot) / 100), 1) - (toolDia / 2.0)

        windings = int((radius + o) / s)
        wRest = round(float((radius + o) % s),2)
        x = cPoint[0]
        y = cPoint[1]
        gc += indent + "G01 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            x,y,feeds["XYGn"], CR
        )
        if dSteps <= 1:
            gc += indent + "G01 Z{0:08.3f} F{1:05.1f} (relative position){2}".format(
                z,feeds["ZGn"], CR
            )
        else:
            gc += indent + "G01 G91 Z{0:08.3f} F{1:05.1f} (relative position){2}".format(
                z,feeds["ZGn"], CR
            )
        orientation = 1     # G02 (CW)
        if dir == "G03":    # G03 (CCW)
            orientation = -1
        x0 = x
        so = i0 = 0.0
        #
        # set start position for first arc
        gc += indent + "G01 G90 X{0:08.3f} F{1:05.1f} (absolute position) {2}".format(
            (x0 + so * -1), feeds["XYGn"], CR
        )
        for w in range(windings):
            loop = ""
            x0 = (s * orientation) * (w+1)
            i0 = (s * orientation) * (w+1)
            #
            # 1. arc (half circle)
            loop += indent + dir + " X{0:08.3f} I{1:08.3f} {2}".format(
                x0, i0, CR
            )
            x0 = x + ((s * orientation) * (w+1)) + (s * orientation)
            i0 = ((0.5 * s) + ((w+1) * s)) * orientation
            #
            # 2. arc radius is half stepover bigger
            loop += indent + dir + " X{0:08.3f} I{1:08.3f} {2}".format(
                x0 * -1 , i0 * -1, CR
            )

            print (loop)
            gc += loop
            pass
        #
        #
        gc += indent + "(-- END current depth --)" + CR
        return gc
