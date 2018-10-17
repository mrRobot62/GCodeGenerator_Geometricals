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
#   This class mill holes in a grid.
#
#   All holes are milled in a circle and not drilled. Use a cutter equal
#   to or smaller than the diameter of the hole.
#
#----------------------------------------------------------------------------
class ContourMillHolesGrid(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        self.__imageNames = [
            # center
            "./img/contour/mill-rect-grid-points.jpg",
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
        choices = [1]

        self.__CC = StringVar()
        self.__CC.set(choices[0])
        self._changeImage(self.__CC.get())
#        Label(self.frmButtonsIndividualContent, text='Coordinate Center').grid(row=row, column=0, sticky=W)
#        OptionMenu(self.frmButtonsIndividualContent,
#            self.__CC, *choices, command=self._changeImage).grid(
#            row=row, column=1)

        row = 0
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
        Label(self.frmButtonsIndividualContent, text='Tool movement').grid(
            row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="on contour", variable=self.__cuttercompensation,
            value="G40").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="left from contour", variable=self.__cuttercompensation,
            value="G41").grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="right from contour", variable=self.__cuttercompensation,
            value="G42").grid(row=row, column=3, sticky=W)

        row += 1
        self.__tooldia = StringVar(value="6.0")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)

        row += 1
        self.__numberOfHolesX = StringVar(value="4")
        self.__numberOfHolesY = StringVar(value="4")
        Label(self.frmButtonsIndividualContent, text="Number of Holes X").grid(
            row=row, column=0, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout", background="Red",
            #vcmd=self._updateAngle,
            textvariable=self.__numberOfHolesX).grid(
                row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Number of Holes Y").grid(
            row=row, column=2, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout", background="Red",
            #vcmd=self._updateAngle,
            textvariable=self.__numberOfHolesY).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__holeRadius = StringVar(value = "10.0")
        self.__gridAngle = StringVar(value = "0.0")
        Label(self.frmButtonsIndividualContent, text="Hole radius (R)").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=True,
            textvariable=self.__holeRadius).grid(
            row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Grid angle (A)").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,  mandatory=True,
            textvariable=self.__gridAngle).grid(
            row=row, column=3, sticky=W)

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
        self.__angle = 0
        self.__distanceA = StringVar(value="10.0")
        self.__distanceB = StringVar(value = "5.0")
        Label(self.frmButtonsIndividualContent, text="Distance between holes (a)").grid(
            row=row, column=0, sticky=W)
        self.__w5 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__distanceA).grid(
            row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Distance between holes (b)").grid(
            row=row, column=2, sticky=W)
        self.__w5 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__distanceB).grid(
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
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    '''
        used to update angle if number of holes changed
    '''
    def _updateAngle(self, nV, **kv):
        print ("update hole angle")
        self.__angle = round(45.0,1)
        if (self.__numberOfHoles.get() > 0):
            # pre set of
            self.__angle = round(360.0 / float(nV),1)
            print ("update angle between holes {0:5.2f} Holes {1}".format(
                self.__angle, nV
            ))
            self.__distanceB.set(str(self.__angle))
        return True


    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):

        # x/y position for circle
        cPoint = (0.0, 0.0) # X/Y entire circle
        hCPoint = (0.0, 0.0) # center hole X/Y


        # radius r = entire Circle, r1= radius per hole
        r1 = float(self.__holeRadius.get())
        r = float(self.__gridAngle.get())
        # tool diameter
        tD = float(self.__tooldia.get())

        # angles
        startAngle = float(self.__distanceA.get())
        holeAngle = float(self.__distanceB.get())

        if (self.validate() == False):
            # an error occured
            return None

        gc = ""
        loop = ""
        # Preamble
        gc += CR + "(set ContourHoles preamble)" + CR
        gc += self._preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        #
        # to make it easier, we calculate everything on center of
        # entiere circle (CC=5) = X/Y = 0.0 + CenterPositions
        cOffset = (0.0, 0.0) # Offset for entire circle X/Y
        hOffset = (0.0, 0.0) # start position including cutter compensation

        if (int(self.__CC.get()) == 1):
            cOffset = (float(self.__centerX.get()), float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 2):
            cOffset = (float(self.__centerX.get()), -float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 3):
            cOffset = (-float(self.__centerX.get()), -float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 4):
            cOffset = (-float(self.__centerX.get()), float(self.__centerY.get()))
        elif (int(self.__CC.get()) == 5):
            cOffset = (float(0.0),float(0.0)) # ignore user input
        else:
            print ("unknown center point choose ({})".format(self.__CC.get()))
            cOffset = (0.0, 0.0)

        # X/Y entire circle
        cPoint = (cOffset[0], cOffset[1])

        # hole X/Y center point
        gc += CR + "(--- START HOLES ---)" + CR
        nHoles = int(self.__numberOfHoles.get())
        sAngle = float(self.__distanceA.get())
        hAngle = float(self.__distanceB.get())
        for h in range(nHoles):
            #
            # calculate first hole x/y center point
            # based on cPoint
            rad = math.radians(sAngle)
            #hX = math.cos(rad) * cPoint[0] +
            hCPoint = (round(math.cos(rad) * r + cPoint[0], 3),
                      round(math.sin(rad) * r + cPoint[1], 3))
            print ("cP {0}, hP {1}".format(cPoint, hCPoint))

            hCPoint = self.__calcCutterComp(r1, tD, hCPoint)
            print ("incl CutterComp cP {0}, hP {1}".format(cPoint, hCPoint))

            hgc = self.generateSubHole(h, sAngle, hCPoint, self.__dir.get())
            gc += hgc + CR
            #
            # next hole angle
            sAngle += hAngle
            pass

        gc += "(--- END HOLES ---)" + CR
        return  gc

    def generateSubHole(self, nr, angle, hCPoint, cDir, retraction="0.5"):
        '''
            create gCode for hole "nr" at point "hCPoint"
            direction of cut is set in "cDir"

        '''
        # gc is local !
        gc = " (--Hole #{0:02d} at angle {1:05.1f}deg --){2}".format(
            int(nr),angle, CR)
        dT = float(self.__depthtotal.get())
        dS = float(self.__depthstep.get())
        dZ = 0.0
        startZ = float(self.__start_Z.get())
        FZ0 = float(self.__speed_Z_G00.get())
        FZ1 = float(self.__speed_Z_G01.get())
        FXY0 = float(self.__speed_XY_G00.get())
        FXY1 = float(self.__speed_XY_G02G03.get())
        X = hCPoint[0]
        Y = hCPoint[1]
        I = float(self.__holeRadius.get()) * -1.0 # X-Offset (radius)
        J = 0.0 # Y-offset
        gc += " " + cDir
        #
        # set start X/Y position
        gc += " X{0:08.3f} Y{1:08.3f} Z{2:08.3f} F{3:05.1f} {4}".format(
            X,Y, startZ, FXY0,CR)
        gc += "  (-- start loop --)" + CR
        lgc = ""
        while (abs(dZ) < abs(dT)):
            #
            # calculate next Z
            if ((abs(dT) - abs(dZ)) < abs(dS)):
                # this happens, if a small amount is the rest
                dZ -= (abs(dT) - abs(dZ))
                print "rest Z: {}".format(dZ)
            else:
                # substract next depthStep
                dZ -= abs(dS)
                print "new Z: {}".format(dZ)

            #
            # before we start next depthstep, we move 0.5 upwards for
            # retraction
            lgc += "  (-- new Z {0:08.3f} --) {1}".format(dZ, CR)
            lgc += "  (retraction)" + CR
            lgc += "  G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                dZ + float(retraction),
                FZ0,
                CR
            )
            #
            # set new Z
            lgc += "  G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                dZ, FZ1, CR)
            # set XZ
            lgc += "  " + cDir
            lgc += " X{0:08.3f} Y{1:08.3f} I{2:08.3f} J{3:08.3f} F{4:05.1f} {5}".format(
                X, Y, I, J, FXY1, CR)
            #
            # for saftey issues.
            if (abs(dZ) == 0.0):
                break
            lgc += CR
            pass
        gc += lgc
        gc += "  (-- end loop --)" + CR + CR
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

    def validate(self):
        r1 = float(self.__holeRadius.get())
        r = float(self.__gridAngle.get())

        tool = float(self.__tooldia.get())
        print ("validate")
        if (r1 > r):
            self.MessageBox("ERROR", "Radius error", "Hole diameter bigger than circle diameter")
            return False

        if (r1 < tool):
            self.MessageBox("ERROR", "Radius error", "Hole diameter smaller than tool diameter")
            return False

        # nothing happens
        return True
