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
#   This class create a holes in a circle.
#
#   All holes are milled in a circle and not drilled. Use a cutter equal
#   to or smaller than the diameter of the hole.
#
#----------------------------------------------------------------------------
class DrillHoles(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        path = "/Users/bernhardklein/Public/local-workspace/python/geometricals/GCodeGenerator_Geometricals/"
        path = "./"
        self.__imageNames = [
            # center
            path + "img/contour/mill-circle-points.png",
        ]

    #-------------------------------------------------------------
    # change image, if an other center point was used
    #-------------------------------------------------------------
    def _changeImage(self, value):
        print len(self.__imageNames)
        i = int(value) - 1
        if (len(self.__imageNames) < i):
            i = len(self.__imageNames) - 1
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
        choices = [1,2,3,4,5]

        self.__CC = StringVar()
        self.__CC.set(choices[4])
        self._changeImage(self.__CC.get())
        Label(self.frmButtonsIndividualContent, text='Coordinate Center').grid(
            row=row, column=0, sticky=W)
        OptionMenu(self.frmButtonsIndividualContent,
            self.__CC, *choices, command=self._changeImage).grid(
            row=row, column=1)

        row += 1
        self.__unit = StringVar()
        self.__unit.set("G21")
        Label(self.frmButtonsIndividualContent, text='Unit').grid(
            row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="mm", variable=self.__unit,
                    value="G21").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="inch", variable=self.__unit,
                    value="G20").grid(row=row, column=2, sticky=W)

        # row += 1
        # self.__dir = StringVar()
        # self.__dir.set("G02")
        # Label(self.frmButtonsIndividualContent, text='Contour direction').grid(
        #     row=row, column=0, sticky=W)
        # Radiobutton(self.frmButtonsIndividualContent, text="CW (G02)", variable=self.__dir,
        #             value="G02").grid(row=row, column=1, sticky=W)
        # Radiobutton(self.frmButtonsIndividualContent, text="CCW (G03)", variable=self.__dir,
        #             value="G03").grid(row=row, column=2, sticky=W)

        row += 1
        # self.__cuttercompensation = StringVar()
        # self.__cuttercompensation.set("G42")
        # Label(self.frmButtonsIndividualContent, text='Tool movement').grid(
        #     row=row, column=0, sticky=W)
        # Radiobutton(self.frmButtonsIndividualContent, text="on contour", variable=self.__cuttercompensation,
        #     value="G40").grid(row=row, column=1, sticky=W)
        # Radiobutton(self.frmButtonsIndividualContent, text="left from contour", variable=self.__cuttercompensation,
        #     value="G41").grid(row=row, column=2, sticky=W)
        # Radiobutton(self.frmButtonsIndividualContent, text="right from contour", variable=self.__cuttercompensation,
        #     value="G42").grid(row=row, column=3, sticky=W)
        #
        row += 1
        self.__tooldia = StringVar(value="6.0")
        self.__numberOfHoles = StringVar(value="4")
        #vcmd = (self.frmButtonsIndividualContent.register(self._updateAngle), '%s', '%S')

        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Number of Holes").grid(
            row=row, column=2, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout",
            vcmd=self._updateAngle,
            textvariable=self.__numberOfHoles).grid(row=row, column=3, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text='Center X').grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Center Y").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerX).grid(row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerY).grid(row=row, column=3, sticky=W)

        row += 1
        self.__circleRadius = StringVar(value = "100.0")
        Label(self.frmButtonsIndividualContent, text="Circle radius (R)").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=True,
            textvariable=self.__circleRadius,
            background="Red").grid(row=row, column=1, sticky=W)

        self.__retraction = StringVar(value = "0.5")
        Label(self.frmButtonsIndividualContent, text="retraction").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=False,
            textvariable=self.__retraction,
            background="Red").grid(row=row, column=3, sticky=W)

        row += 1
        self.__angle = 0
        self.__initialStartAngle = StringVar(value=self.__angle)
        # this field is self calculated
        self.__holeAngle = StringVar(value = self.__initialStartAngle.get())
        Label(self.frmButtonsIndividualContent, text="Initial start angle").grid(
            row=row, column=0, sticky=W)
        self.__w5 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__initialStartAngle).grid(
            row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Angle between holes").grid(
            row=row, column=2, sticky=W)
        Label(self.frmButtonsIndividualContent, textvariable=self.__holeAngle).grid(
            row=row, column=3, sticky=W)

        row += 1
        self.__depthtotal = StringVar(value="-10.5")
        self.__depthstep = StringVar(value="-0.5")
        Label(self.frmButtonsIndividualContent, text="Total depth").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__depthtotal, mandatory=True).grid(
            row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="depth cutting per step").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__depthstep, mandatory=True).grid(
            row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G00 = StringVar(value="300.0")
        self.__speed_Z_G00 = StringVar(value="250.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G00 X/Y)").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G00 Z)").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_XY_G00, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_Z_G00, mandatory=False).grid(row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G02G03 = StringVar(value="250.0")
        self.__speed_Z_G01 = StringVar(value="150.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G02/G03 X/Y)").grid(row=row, column=0, sticky=W)
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

        #row += 1
        self.__safety_Z = StringVar(value="10.0")
        Label(self.frmButtonsIndividualContent, text="Safety Z:").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__safety_Z, mandatory=False).grid(
            row=row, column=3, sticky=W)

        #-----------------------------------------------------
        self._updateAngle(self.__numberOfHoles.get())
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    def _updateAngle(self, numberOfHoles, **kv):
        '''
            used to update angle if number of holes changed
        '''
        if (self.__numberOfHoles.get() > 0):
            # pre set of
            holeAngle = round(360.0 / float(numberOfHoles),1)
            print ("update angle between holes {0:5.2f} Holes {1}".format(
                holeAngle, numberOfHoles
            ))
            self.__holeAngle.set(str(holeAngle))

        return True


    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):

        # x/y position for circle
        cPoint = (0.0, 0.0) # X/Y entire circle
        numberOfHoles = int(self.__numberOfHoles.get())

        # radius r = entire Circle
        radius = float(self.__circleRadius.get())
        peckCycle = float(self.__retraction.get())

        # tool diameter
        tD = float(self.__tooldia.get())

        # angles
        startAngle = float(self.__initialStartAngle.get())
        deg = float(self.__holeAngle.get())
        feeds = {
            "XYG0" : float(self.__speed_XY_G00.get()),
            "XYGn" : float(self.__speed_XY_G02G03.get()),
            "ZG0" : float(self.__speed_Z_G00.get()),
            "ZGn" : float(self.__speed_Z_G01.get())
        }

        zPos = {
            "safetyZ" : float(self.__safety_Z.get()),
            "startZ" : float(self.__start_Z.get())
        }

        # dir
        dir = 0
        # if (self.__dir.get() == "G02"):
        #     dir = 0 #CW G02
        # else :
        #     dir = 1 #CCW G03

        #
        # to make it easier, we calculate everything on center of
        # entiere circle (CC=5) = X/Y = 0.0 + CenterPositions

        if (int(self.__CC.get()) == 1):
            cPoint = (float(self.__centerX.get()), float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 2):
            cPoint = (float(self.__centerX.get()), -float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 3):
            cPoint = (-float(self.__centerX.get()), -float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 4):
            cPoint = (-float(self.__centerX.get()), float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 5):
            cPoint = (float(0.0),float(0.0)) # ignore user input
        else:
            print ("unknown center point choose ({})".format(self.__CC.get()))
            cPoint = (0.0, 0.0)

#    def __calculateHoleCPoints(self, numberOfHoles, cPoint, r, angle, deg):

        hCPoint = self.__calculateHoleCPoints(
            numberOfHoles,
            cPoint,
            radius,
            startAngle,
            deg
        )

        loop = ""
        gc = ""
        gc += self.getGCode_Preamble()
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
             float(self.__safety_Z.get()),
             float(self.__speed_Z_G00.get()), CR)
        gc += "(--- START HOLES ---)" + CR
        indent = "".ljust(2)
        h = 0
        for v in hCPoint:
            # loop += "G01 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            #     v[0], v[1],
            #     feeds["XYGn"],
            #     CR
            # )
            # if peckCycle > 0.0:
            #     loop += "G01 Z+{0:08.3f} {1}".format(
            #         (z + peckCycle), CR
            #     )
            loop += self.__drillHole(h, v, radius, feeds, indent, peckCycle)
            h += 1

        gc += loop
        gc += "(--- END HOLES ---)" + CR
        gc += "(-- homeing --)" + CR
        print "Homing"
        gc += self.getGCode_Homeing(
            cPoint[0],
            cPoint[1],
            zPos["safetyZ"],
            feeds["XYG0"]
        )
        gc += self.getGCode_Postamble()
        gc += CR
        return  gc

    def __drillHole(self, nr, vec, r, feeds, indent = "", retraction="0.5"):
        # gc is local !
        gc = indent + "(--drill hole #{0:02d} at pos {1} --) {2}".format(
            nr, vec, CR)

        depthZ = (float(self.__depthtotal.get()), float(self.__depthstep.get()))
        dZ = 0.0
        dwell = 0.25

        zPos = {
            "safetyZ"   : float(self.__safety_Z.get()),
            "startZ"    : float(self.__start_Z.get())
        }

        #
        # set start X/Y position
        gc += indent + "G00 Z{0:08.3f}{1}".format(
            zPos["startZ"], CR)
        gc += indent + "G00 X{0:08.3f} Y{1:08.3f} {2}".format(
            vec[0], vec[1], CR)
        gc += indent + "(-- start Z loop total {0} step {1}--) {2}".format(
            depthZ[0], depthZ[1], CR
        )
        lgc = ""
        indent2 = indent.ljust(len(indent) + 2)
        if (retraction == ""):
            retraction = "0.0"
        while (abs(dZ) < abs(depthZ[0])):
            #
            # calculate next Z
            if ((abs(depthZ[0]) - abs(dZ)) < abs(depthZ[1])):
                # this happens, if a small amount is the rest
                dZ -= (abs(depthZ[0]) - abs(dZ))
                print "#{0} rest Z: {1}".format(nr, dZ)
            else:
                # substract next depthStep
                dZ -= abs(depthZ[1])
                print "#{0} new Z: {1}".format(nr, dZ)

            #
            # before we start next depthstep, we move 0.5 upwards for
            # retraction
            lgc += indent2 + "(-- new Z {0:08.3f} --) {1}".format(dZ, CR)

            #
            # set new Z
            lgc += indent2 + "(drill)" + CR
            lgc += indent2 + "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
                dZ, feeds["ZGn"], CR)
            #
            # pause a short period
            lgc += indent2 + "G04 P{0:04.2f} {1}".format(dwell, CR)
            lgc += indent2 + "(retraction)" + CR
            lgc += indent2 + "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
                dZ + float(retraction),
                feeds["ZG0"],
                CR
            )
            # # set XZ
            # lgc += indent2 + "G01 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            #     vec[0], vec[1], feeds["XYGn"], CR)
            #
            # for saftey issues.
            if (abs(dZ) == 0.0):
                break
            lgc += CR
            pass

        gc += lgc
        gc += indent + "(-- end loop --)" + CR + CR
        gc += CR
        return gc

    def __calculateHoleCPoints(self, numberOfHoles, cPoint, r, angle, deg):
        '''
        This method calculate for all holes the center point due to
        starting angle. First Circle is from right the first in +y

         /--2--\
        /       \
        3       1       0 degrees
        \       /
         \--4--/

        radius = radius center Circle
        cPoint[0] = center X point of center Circle
        cPoint[1] = center Y point of center Circle
        angle = angle of first hole
        deg = degrees to next hole

        '''
        hcp = []
        #r = radius
        for x in range (numberOfHoles):
            rad = math.radians(angle)
            # set X point
            v = (round(math.cos(rad) * r + cPoint[0], 3),
                round(math.sin(rad) * r + cPoint[1], 3))
            hcp.append(v)
            print "Hole center points {0} on radius {1:05.1f} angle {2:05.1f}".format(
                v, r, angle)
            angle += deg

        return hcp

    def userInputValidation(self):
        r = float(self.__circleRadius.get())

        tD = float(self.__depthtotal.get())
        sD = float(self.__depthstep.get())

        pC = float(self.__retraction.get())

        tool = float(self.__tooldia.get())
        print ("userInputValidation")

        if (r <= 0.0 ):
            self.MessageBox("ERROR", "Radius error",
                "radius hove to be greater than 0.0")
            return False

        if (r < tool):
            self.MessageBox("ERROR", "Radius error",
            "Hole diameter {} smaller than tool diameter {}".format(r,tool))
            return False

        if (pC < 0.0):
            self.MessageBox("ERROR", "Peck Cycle error",
            "Peck cycle should be a positive value (0.00 - {})".format(pC))
            return False

        if (pC > tool):
            self.MessageBox("ERROR", "Peck Cycle error",
            "Peck cycle {} should be less than tool diameter (0.00 - {})".format(
                pC, tool))
            return False

        if (tool <= 1.0):
            self.MessageBox("ERROR", "Tool error",
            "Too diamater {} have to be greater as 1.0".format(tool))
            return False

        if (tD >= 0.0 or sD > 0.0):
            self.MessageBox("ERROR", "Depth error",
            "Total depth {} and depth step {}should be a negative value".format(
                tD, sD
            ))
            return False

        if (abs(tD) < abs(sD)):
            self.MessageBox("ERROR", "Depth error",
            "Total depth {} should be greater than depth step {}".format(
                tD, sD
            ))
            return False

        # nothing happens
        return True
