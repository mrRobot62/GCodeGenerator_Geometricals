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
        self.__numberOfHolesY = StringVar(value="3")
        Label(self.frmButtonsIndividualContent, text="Number of Holes X").grid(
            row=row, column=0, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout", background="Red",
            textvariable=self.__numberOfHolesX).grid(
                row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Number of Holes Y").grid(
            row=row, column=2, sticky=W)
        IntegerEntry(self.frmButtonsIndividualContent, width=10,
            mandatory=True, validate="focusout", background="Red",
            textvariable=self.__numberOfHolesY).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__holeRadius = StringVar(value = "5.0")
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
        self.__distanceA = StringVar(value="15.0")
        self.__distanceB = StringVar(value = "15.0")
        Label(self.frmButtonsIndividualContent, text="Distance rows (a)").grid(
            row=row, column=0, sticky=W)
        self.__w5 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__distanceA).grid(
            row=row, column=1, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Distance columns (b)").grid(
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


    #-------------------------------------------------------------
    # here you generate your GCode.
    # some of this code should be used every time.
    # insert your code bettween marked rows
    #-------------------------------------------------------------
    def generateGCode(self):

        # x/y position for circle
        cPoint = (0.0, 0.0) # general Centerpoint of hole #1
        hCPoints = (0.0, 0.0) # center of current milled hole
        gSize = (0.0, 0.0) # hole distances a & b

        zPos = {
            "safetyZ" : float(self.__safety_Z.get()),
            "startZ" : float(self.__start_Z.get())
        }

        feeds = {
            "XYG0" : float(self.__speed_XY_G00.get()),
            "XYGn" : float(self.__speed_XY_G02G03.get()),
            "ZG0" : float(self.__speed_Z_G00.get()),
            "ZGn" : float(self.__speed_Z_G01.get())
        }

        # radius r = entire Circle, r1= radius per hole
        r = float(self.__holeRadius.get())
        # tool diameter
        tD = float(self.__tooldia.get())
        row = float(self.__distanceA.get())
        col = float(self.__distanceB.get())

        X = float(self.__centerX.get())
        Y = float(self.__centerY.get())

        gSize = (row,col)

        # grid angle (A)
        gridAngle = round(float(self.__gridAngle.get()),1)

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
        # milling of every hole starts on a 45degr angle

        cOffset = (0.0, 0.0) # Offset for entire circle X/Y
        hOffset = (0.0, 0.0) # start position including cutter compensation

        #
        # lets assume we start for the first hole on X/Y position

        # X/Y entire circle
        cPoint = (X,Y)

        hCPoints = self.createHoleCenterPointVectorList(cPoint, gSize, gridAngle)
        print "hCPoints {}".format(hCPoints)
        hCPoints = self.addCutterCompensation(hCPoints, tD, r)
        print "with cutter compensation hCPoints {}".format(hCPoints)

        # hole X/Y center point
        gc += CR + "(--- START HOLES ---)" + CR
        nr = 0
        intend = "".ljust(2)
        for vc in hCPoints:
            nr += 1
            gc += self.generateSubHole(
                nr, gridAngle, vc, self.__dir.get(), intend)
            pass

        gc += "(--- END HOLES ---)" + CR
        gc += self.getGCode_Homeing(
            cPoint[0],
            cPoint[1],
            zPos["safetyZ"],
            feeds["XYG0"]
        )
        gc += self._postamble.get() + CR
        gc += CR
        return  gc

    def createHoleCenterPointVectorList(self, cPoint, gSize, gAngle, colOffsetX=0.0):
        '''
        based on CPoint this method create for all holes the center point
        This vector list is later on used to calculate starting milling position
        due to cutter compensation

        return hCPoint center point for every hole
        '''
        numberOfHolesX = int(self.__numberOfHolesX.get())
        numberOfHolesY = int(self.__numberOfHolesY.get())

        hCPoints = []
        #
        # to avoid over shoots
        if gAngle < 0.0 or gAngle > 90.0:
            gAngle = 0.0

        #
        # initialize point vector list
        cPointTemp = cPoint
        distRow = distCol = 0.0
        intend = "".ljust(2)

        cPX = cPY = distRow = distCol = 0.0
        cColOffset = (0.0, 0.0)
        for y in range (numberOfHolesY):
            cPX = cPY = 0.0
            print (CR + "Row #{0} grid Angle {1:5.1f}, colOffsetX {2:5.1f}".format(
                (y+1), gAngle, colOffsetX)
            )

            gamma = 90
            alpha = gAngle
            beta = gamma - alpha

            dRow = (gSize[0] * y)
            #
            # this triangle is needed to calculate the new center point
            # for next drill hole
            sideA = round(dRow * math.cos(math.radians(beta)),3)
            sideB = round((math.sqrt(math.pow(dRow, 2) - math.pow(sideA, 2))),3)
            sideC = round(gSize[0], 3) #a
            #
            # below calculation is neede for all rows above themes
            # first row and only if gridAngle is > 0.0
            # because if we turn the grid for x degrees, than a
            # little triangle can be calculated. The hypernuse of this
            # triangle is distance ROW (a), in this case side "a" of This
            # triangle is the distance between current X and new X. New X
            # is every time left from current X
            #
            # side b of triangle is the distance vorm current Y and next Y
            # and every time above current Y
            #
            if y > 0 and gAngle > 0.0:
                print ("1) cPoint ({})".format(cPoint))
                # next xPoint is left from last xPoint
                # next yPoint is up from last yPoint
                cPoint = ((cPointTemp[0] - sideA),(cPointTemp[1] + sideB))
                print ("2) cPoint ({})".format(cPoint))
                print "Triangle a({})  b({})  c({})  alpa({})  beta({})  gamma({})".format(
                    sideA, sideB, sideC, alpha, beta, gamma
                )
                cColOffset = self.__setOffsetX(
                    colOffsetX,
                    gAngle)

                cPoint = (
                    cPoint[0] + cColOffset[0],
                    cPoint[1] + cColOffset[1])
                pass

            distCol = 0.0
            for x in range(numberOfHolesX):
                print ("Hole #{0} cPX{1}. cPY{2} sA {3} sB {4} sC {5}".format(
                    ((x+1) + (y*numberOfHolesX)),
                    cPX, cPY, sideA, sideB, sideC))
                #
                # for every "first" hole in a row, some special
                # calculations are needed
                if (x == 0):
                    # add/sub calculated triangle sides a + b from
                    # current Centerpoint
                    if (gAngle > 0.0):
                        cPY += (sideB + cColOffset[1])
                        cPX -= sideA
                        cPX += cColOffset[0]
                    else:
                        cPY += dRow
                else:
                    distCol += gSize[1] #b
                    rad = math.radians(gAngle)
                    #
                    # sin/cos is calculated every time with gSize(b) (distCol)
                    cPX = round(math.cos(rad) * (gSize[1] * x) + cPoint[0], 3)
                    cPY = round(math.sin(rad) * (gSize[1] * x) + cPoint[1], 3)

                    # if gridAngle = 0.=, than y is every time distance b
                    if (gAngle == 0.0):
                        cPY += dRow
                    #
                    # add this vector
                #
                # offset is only relevant for above rows !
                if (y > 0):
                    cColOffset = self.__setOffsetX(
                        colOffsetX,
                        gAngle)

                    print("--> (a) Offset cPX {}, cPY {}, colOffset {} ".format(cPX, cPY, cColOffset))
                    cPY += cColOffset[1]
                    if (gAngle == 0.0):
                        cPX += (cColOffset[0] * y)
                    else:
                        cPX += cColOffset[0]
                    print("--> (b) Offset cPX {}, cPY {}, colOffset {} ".format(cPX, cPY, cColOffset))
                    pass

                hCPoints.append((round(cPX,3), round(cPY,3)))

                #
                print ("   new cPX {0} cPY {1}, distRow {2}, distCol {3}".format(
                    cPX, cPY, distRow, distCol))
                pass
            distRow += gSize[0] #a
            pass

        return hCPoints

    def __setOffsetX(self, offset, gAngle):
        x = y = 0.0

        gamma = 90
        alpha = gAngle
        beta = gamma - alpha

        #
        # this triangle is needed to calculate the new center point
        # for next drill hole
        sideA = round(offset * math.cos(math.radians(beta)),3)
        sideB = round((math.sqrt(math.pow(offset, 2) - math.pow(sideA, 2))),3)
        sideC = round(offset, 3) #a

        x += sideB
        y += sideA

        print ("CalcOffset x {}, y {}".format(x,y))
        return (x,y)


    def addCutterCompensation(self, hCPoints, toolDia, holeRadius):
        '''
        if cutter compenstation is needed, this method set the real starting
        point for milling including compensation (inside, outside, cneter)
        based on current tool diameter
        '''
        gc = ""
        r = toolDia/2.0
        hcp = []
        for v in hCPoints:
#            print ("->(a) V {}".format(v))
#            v = (v[0]+(holeRadius/2.0),v[1])
#            print ("->(b) V {}".format(v))
            if (self.__cuttercompensation.get() == "G40"):
                hcp.append(v)
                pass
            if (self.__cuttercompensation.get() == "G41"):
                hcp.append((v[0] - r,v[1]) )
            if (self.__cuttercompensation.get() == "G42"):
                hcp.append((v[0] + r,v[1]) )
        return hcp

    def generateSubHole(self, nr, angle, hCPoint, cDir, intend="", retraction=0.0):
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
        saveZ = float(self.__safety_Z.get())
        FZ0 = float(self.__speed_Z_G00.get())
        FZ1 = float(self.__speed_Z_G01.get())
        FXY0 = float(self.__speed_XY_G00.get())
        FXY1 = float(self.__speed_XY_G02G03.get())
        X = hCPoint[0]
        Y = hCPoint[1]
        I = float(self.__holeRadius.get()) * -1.0 # X-Offset (radius)
        J = 0.0 # Y-offset
        gc += intend
        #
        # set start X/Y position
        gc += intend + "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
            startZ, FZ1,CR
        )
        gc += intend + "G01 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            X, Y, FXY1, CR)
        gc += intend + "(-- start loop --)" + CR
        lgc = ""
        intend2 = intend.ljust(2)
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
            if retraction > 0.0:
                lgc += intend2 + "(-- new Z {0:08.3f} --) {1}".format(dZ, CR)
                lgc += intend2 + "(retraction)" + CR
                lgc += intend2 + "G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                    dZ + retraction,
                    FZ0,
                    CR
                )
            #
            # set new Z
            lgc += intend2 + "G01 Z{0:08.3f} F{1:04.0f} {2}".format(
                dZ, FZ1, CR)
            # set XZ
            lgc += intend2 + cDir
            lgc += " X{0:08.3f} Y{1:08.3f} I{2:08.3f} J{3:08.3f} F{4:05.1f} {5}".format(
                X, Y, I, J, FXY1, CR)
            #
            # for saftey issues.
            if (abs(dZ) == 0.0):
                break
            lgc += CR
            pass
        gc += lgc
        # start Z
        gc += intend + "G00 Z{0:08.3f} F{1:04.0f} {2}".format(
            startZ, FZ0, CR)
        gc += intend + "(-- end loop --)" + CR + CR
        return gc

    def userInputValidation(self):
        '''
        this class is used to validate necessary user input fields
        '''
        print ("userInputValidation")
        hR = float(self.__holeRadius.get())
        gA = float(self.__gridAngle.get())
        a = float(self.__distanceA.get())
        b = float(self.__distanceB.get())
        nHX = float(self.__numberOfHolesX.get())
        nHY = float(self.__numberOfHolesY.get())
        toolDia = float(self.__tooldia.get())

        if (nHX <= 0.0 or nHY <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="number of holes in X and Y should be 1 or more")
            return False

        if (gA < 0.0 or gA > 90.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="grid angle should be between 0.0 and 90.0")
            return False

        if (toolDia <= 0.0 ):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tool diamater should be greater than 0.0")
            return False

        if (hR <= (toolDia/2) and hR >= 0.0 ):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="hole radius greater than tool diameter and 0.0")
            return False

        if ((hR*2) >= a or (hR*2) >= b):
            self.MessageBox(state="ERROR",
                title="WARN",
                text="hole diameter is greater than distance a or b")
            return False

        if (a <= 0.0 or b <= 0.0):
            self.MessageBox(state="ERROR",
                title="WARN",
                text="distances A and B should be greater than 0.0")
            return False

        if (a <= (hR*2) or b <= (hR*2)):
            self.MessageBox(state="ERROR",
                title="WARN",
                text="distance A or B is less than hole diameter")
            return False

        if (float(self.__centerX.get()) < 0.0 or float(self.__centerY.get()) < 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Values for CenterX/Y should be positive")
            return False

        if (abs(float(self.__depthtotal.get())) < abs(float(self.__depthstep.get()))):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tooldiamter should be less than arc diameter")
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
