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
class ContourHoles(GeometricalFrame):

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
                    value="G03").grid(row=row, column=2, sticky=W)

        row += 1
        self.__cuttercompensation = StringVar()
        self.__cuttercompensation.set("G42")
        Label(self.frmButtonsIndividualContent, text='Tool movement').grid(row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="on contour", variable=self.__cuttercompensation,
            value="G40").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="left from contour", variable=self.__cuttercompensation,
            value="G41").grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="right from contour", variable=self.__cuttercompensation,
            value="G42").grid(row=row, column=3, sticky=W)

        row += 1
        self.__tooldia = StringVar(value="3.0")
        self.__numberOfHoles = StringVar(value="4")
        #vcmd = (self.frmButtonsIndividualContent.register(self._updateAngle), '%s', '%S')

        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Number of Holes").grid(row=row, column=2, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout",
            vcmd=self._updateAngle,
            textvariable=self.__numberOfHoles).grid(row=row, column=3, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text='Center X').grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Center Y").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerX).grid(row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__centerY).grid(row=row, column=3, sticky=W)

        row += 1
        self.__holeRadius = StringVar(value = "10.0")
        self.__circleRadius = StringVar(value = "100.0")
        Label(self.frmButtonsIndividualContent, text="Hole radius (R1)").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=True,
            textvariable=self.__holeRadius,
            background="Red").grid(row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Circle radius (R)").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=True,
            textvariable=self.__circleRadius,
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
        self.__speed_Z_G00 = StringVar(value="100.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G00 X/Y)").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G00 Z)").grid(row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_XY_G00, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_Z_G00, mandatory=False).grid(row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G02G03 = StringVar(value="100.0")
        self.__speed_Z_G01 = StringVar(value="80.0")
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

        # radius r = entire Circle, r1= radius per hole
        radii = (float(self.__circleRadius.get()),
                float(self.__holeRadius.get()))

        # tool diameter
        tD = float(self.__tooldia.get())

        # angles
        startAngle = float(self.__initialStartAngle.get())
        holeAngle = float(self.__holeAngle.get())

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
        if (self.__dir.get() == "G02"):
            dir = 0 #CW G02
        else :
            dir = 1 #CCW G03

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


        hCPoint = self.__calculateHoleCPoints(
            numberOfHoles,
            cPoint,
            radii,
            startAngle,
            holeAngle
        )

        hCPoint = self.__addCutterCompensation(
            hCPoint, radii, tD, dir
        )

        gc = ""
        loop = ""
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
        dir = self.__dir.get()
        h = 0
        for v in hCPoint:
            loop += self.__generateSubHole(h, v, radii, feeds, dir, indent, retraction="0.0" )
            h += 1

        gc += loop
        gc += "(--- END HOLES ---)" + CR

        gc += self.getGCode_Homeing(
            cPoint[0],
            cPoint[1],
            zPos["safetyZ"],
            feeds["XYG0"]
        )
        gc += self.getGCode_Postamble()
        gc += CR
        return  gc

    def __calculateHoleCPoints(self, numberOfHoles, cPoint, radii, angle, deg):
        '''
        This method calculate for all holes the center point due to
        starting angle. First Circle is from right the first in +y

         /--2--\
        /       \
        3       1       0 degrees
        \       /
         \--4--/

        radii[0] = radius center Circle
        radii[1] = radius per hole
        cPoint[0] = center X point of center Circle
        cPoint[1] = center Y point of center Circle
        angle = angle of first hole
        deg = degrees to next hole

        '''
        hcp = []
        r = radii[0]
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

    def __addCutterCompensation(self, hCPoint, radii, toolDia, dir):
        '''
            this method add the cutter compensation to hole center points
            due to tool diameter and G40 / G41 / G42

            hCPoint vector list contain for all holes the center points
            For every hole we go the the most left contour and calculated
            cutter compensation

            G41 is left from this contour. If used, we set the tool outside
            G42 is right from this contour. If used, we set the tool inside
        '''
        hcp = []
        tR = (toolDia / 2.0 )
        hR = radii[1]
        cutterComp = 0
        if (self.__cuttercompensation.get() == "G41"):
            # left from contour
            cutterComp = 1
        elif (self.__cuttercompensation.get() == "G42"):
            # right from contour
            cutterComp = 2
        else:
            # no cutter compensation, mill on contour e.g G40
            return hCPoint
        h = 0
        for v in hCPoint:
            if cutterComp == 1:
                # left from contour (outside of contour)
                v = (v[0] - hR - tR, v[1])
            else:
                # right from contour (inside hole)
                v = (v[0] - hR + tR, v[1])

            hcp.append(v)
            print "Set cutter compensation #{0} XY{1}".format(h,v)
            h += 1
        return hcp

    def __generateSubHole(self, nr, vec, radii, feeds, dir, indent = "", retraction="0.5"):
        '''
            create gCode for hole "nr" at point "hCPoint"
            direction of cut is set in "cDir"

        '''
        # gc is local !
        gc = indent + "(--Hole #{0:02d} at pos {1} --){2}".format(
            nr, vec, CR)

        depthZ = (float(self.__depthtotal.get()), float(self.__depthstep.get()))
        dZ = 0.0

        zPos = {
            "safetyZ"   : float(self.__safety_Z.get()),
            "startZ"    : float(self.__start_Z.get())
        }


        # radii[0] = center radius
        # radii[1] = hole radius
        I = radii[1] * -1.0 # X-Offset (radius)
        J = 0.0 # Y-offset

        #
        # set start X/Y position
        gc += indent + "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
            zPos["startZ"], feeds["XYGn"],CR)
        gc += indent + "G01 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            vec[0], vec[1], feeds["XYGn"],CR)
        gc += indent + "(-- start Z loop total {0} step {1}--) {2}".format(
            depthZ[0], depthZ[1], CR
        )
        lgc = ""
        indent2 = indent.ljust(2)
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
            lgc += indent2 + "(retraction)" + CR
            lgc += indent2 + "G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                dZ + float(retraction),
                feeds["ZG0"],
                CR
            )
            #
            # set new Z
            lgc += indent2 + "G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                dZ, feeds["ZGn"], CR)
            # set XZ
            lgc += indent2 + dir
            lgc += " X{0:08.3f} Y{1:08.3f} I{2:08.3f} J{3:08.3f} F{4:05.1f} {5}".format(
                vec[0], vec[1], I, J, feeds["XYGn"], CR)
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

    def __calcCutterComp(self, hR, tD, hCPoint):
        '''
        if cutter compensation is used, than X/Y position for milling
        should be recalculated.
        This method return a vector for (x/y) which should be added to
        current X/Y position

        hR      = hole Radius
        tD      = tool diameter
        hCPoint = center point of hole

        Example: hCPoint X/Y = (0.0, 0.0)
            Cutter Dia: 8mm, mill Dir = CW

            Example CW


        '''
        # we assume, that every time, we have to set the mill to a 45deg
        # angle from center point
        rad = math.radians(45.0)
        tR = tD / 2.0
        r = hR - tR
        hCPointNew = (round(math.cos(rad) * r + hCPoint[0], 3),
                  round(math.sin(rad) * r + hCPoint[1], 3))
        print ("tR {2} hCP {0}, hCPn {1}".format(hCPoint, hCPointNew, hR))

        tR = round((float(self.__tooldia.get()) / 2.0 ),1)

        if (self.__cuttercompensation.get() == "G40"):
            v = (0.0, 0.0)
        if (self.__cuttercompensation.get() == "G41"):
            v = (tR, tR)
        if (self.__cuttercompensation.get() == "G42"):
            v = (-tR, -tR)
        if (self.__dir.get() == "G03"):
            #CW
            v = (v[0] * 1.0, v[1] * 1.0)
        else:
            # G03 = CCW
            v = (v[0] * -1.0, v[1] * -1.0)

        v = (hCPoint[0] + v[0],
             hCPoint[1] + v[1])

        print ("Cutter compensation vector ({})".format(v))
        return v

    def userInputValidation(self):
        r1 = float(self.__holeRadius.get())
        r = float(self.__circleRadius.get())

        tD = float(self.__depthtotal.get())
        sD = float(self.__depthstep.get())

        tool = float(self.__tooldia.get())
        print ("userInputValidation")

        if (r <= 0.0 or r1 <= 0.0):
            self.MessageBox("ERROR", "Radius error",
                "radius hove to be greater than 0.0")
            return False

        if (r1 > r):
            self.MessageBox("ERROR", "Radius error",
                "Hole diameter bigger than circle diameter")
            return False

        if (r1 < tool):
            self.MessageBox("ERROR", "Radius error",
            "Hole diameter smaller than tool diameter")
            return False

        if (tool <= 1.0):
            self.MessageBox("ERROR", "Tool error",
            "Too diamater have to be greater as 1.0")
            return False

        if (tD >= 0.0 or sD > 0.0):
            self.MessageBox("ERROR", "Depth error",
            "Total depth and depth step should be a negative value")
            return False

        if (abs(tD) < abs(sD)):
            self.MessageBox("ERROR", "Depth error",
            "Total depth should be greater than depth step")
            return False

        # nothing happens
        return True
