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
class DialogContourRoundedRec(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        path = "/Users/bernhardklein/Public/local-workspace/python/geometricals/GCodeGenerator_Geometricals/"
        path = "./"
        self.__imageNames = [
            # left down
            path + "img/contour/round-rectangle-pic1_1.jpg",
            path + "img/contour/round-rectangle-pic1_2.jpg",
            path + "img/contour/round-rectangle-pic1_3.jpg",
            path + "img/contour/round-rectangle-pic1_4.jpg",
            path + "img/contour/round-rectangle-pic1_5.jpg",
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
        #choices = [1,2,3]
        choices = [1, 2, 3, 4, 5]

        self.__CC = StringVar()
        self.__CC.set(choices[4])
        self._changeImage(self.__CC.get())
        # new in V012.5 --
        self.setMaterialDict(self.selectedMaterial.get())
        #-----------------
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
            value=1).grid(
                row=row, column=2, sticky=W)

        row += 1
        self.__cuttercompensation = StringVar()
        self.__cuttercompensation.set("G40")
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

        td = self.dicSelectedMaterial["Tool dia"]
        print("ToolDia: " + str(td))
        self.tooldia = StringVar(value=str(td))
        Label(
            self.frmButtonsIndividualContent, text="Tool diameter").grid(
                row=row, column=0, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            mandatory=False,
            textvariable=self.tooldia).grid(
                row=row, column=1, sticky=W)

        #row += 1
        self.__radius = StringVar(value="10.0")
        Label(
            self.frmButtonsIndividualContent, text="Edge radius (R)").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            mandatory=False,
            textvariable=self.__radius).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__centerX = StringVar(value="0.0")
        self.__centerY = StringVar(value="0.0")
        Label(
            self.frmButtonsIndividualContent, text='Center X').grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent, text='Center Y').grid(
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

        row += 1
        self.__distanceA = StringVar(value="70.0")
        self.__distanceB = StringVar(value="100.0")
        Label(
            self.frmButtonsIndividualContent, text="Height (a)").grid(
                row=row, column=0, sticky=W)
        Label(
            self.frmButtonsIndividualContent, text="Width (b)").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__distanceA).grid(
                row=row, column=1, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=5,
            textvariable=self.__distanceB).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__depthtotal = StringVar(value="-1.5")
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
        self.speed_XY_G02G03 = StringVar(value="80.0")
        self.speed_Z_G01 = StringVar(value="50.0")
        Label(
            self.frmButtonsIndividualContent, text="Feed (G01 X/Y)").grid(
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
            self.frmButtonsIndividualContent, text="Safety Z").grid(
                row=row, column=2, sticky=W)
        FloatEntry(
            self.frmButtonsIndividualContent,
            width=10,
            textvariable=self.__safety_Z,
            mandatory=False).grid(
                row=row, column=3, sticky=W)

        #-----------------------------------------------------
        self.upateMaterialFields(self.selectedMaterial.get())
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    def userInputValidation(self):
        '''
        this class is used to validate necessary user input fields
        '''
        print("userInputValidation")
        gR = float(self.__radius.get())
        a = float(self.__distanceA.get())
        b = float(self.__distanceB.get())
        toolDia = float(self.tooldia.get())

        if (gR < 0.0):
            self.MessageBox(
                state="ERROR",
                title="ERROR",
                text="edge radius should be greater or equal 0.0")
            return False

        if (a <= 0.0 or b <= 0.0):
            self.MessageBox(
                state="ERROR",
                title="ERROR",
                text="a and b should be greater than 0.0")
            return False

        if (abs(float(self.__depthtotal.get())) < abs(
                float(self.__depthstep.get()))):
            self.MessageBox(
                state="ERROR",
                title="ERROR",
                text="Total depth should be deeper or equal depth step")
            return False

        if (float(self.__start_Z.get()) <= 0.0
                or float(self.__safety_Z.get()) <= 0.0):
            self.MessageBox(
                state="ERROR",
                title="ERROR",
                text="Z parameter values should be greater than 0.0")
            return False

        if (float(self.tooldia.get()) <= 0.0):
            self.MessageBox(
                state="ERROR",
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
        generate GCode for a rounded rectangle.
        This class is copied from pocketRoundRectangle. Some unnessesary
        code are removed. Some parts are new (cutter compensation)
        '''
        cPoint = (float(self.__centerX.get()), float(self.__centerY.get()))
        sizeAB = (float(self.__distanceA.get()), float(self.__distanceB.get()))
        radius = float(self.__radius.get())
        toolDia = float(self.tooldia.get())

        zPos = {
            "safetyZ": float(self.__safety_Z.get()),
            "startZ": float(self.__start_Z.get())
        }

        depth = (
            float(self.__depthtotal.get()),
            float(self.__depthstep.get()),
        )

        dir = self.__dir.get()

        feeds = {
            "XYG0": float(self.__speed_XY_G00.get()),
            "XYGn": float(self.speed_XY_G02G03.get()),
            "ZG0": float(self.__speed_Z_G00.get()),
            "ZGn": float(self.speed_Z_G01.get())
        }
        gc = ""
        gc += self.getGCode_Preamble()
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(zPos["safetyZ"],
                                                     feeds["ZG0"], CR)

        #
        # even which center point user choosed, we start on
        # center point object - left down (5)

        # set start postion X/Y
        gc += CR + "(set center position)" + CR
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            cPoint[0], cPoint[1], feeds["XYG0"], CR)
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
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(zPos["startZ"],
                                                     feeds["ZG0"], CR)
        spaces = "".ljust(2)
        #----------------------------------------------------------------------
        # This loop asume, that you try to mill into your object.
        # if not needed for your shape, remove this part and rewrite
        #----------------------------------------------------------------------
        #

        pocketMillTracks = []
        x = 1
        t = self.__createPocketTracks(
            cPoint,
            sizeAB,
            radius,
            feeds,
            0.0  # no offset, milling only one time !
        )
        pocketMillTracks.append(t)
        gc += self.getGCodeCutterComp(self.__cuttercompensation.get(), toolDia)

        #
        # it's time to generate the real gCode
        #
        # Every round we mill all tracks in the same detph
        # than we increase depth as long as we reached total depthStep

        gc += CR + "(-- START DEPTH Loop --)" + CR
        z = depth[1]
        while (abs(z) < abs(depth[0])):
            # set next Z depth
            if ((abs(depth[0]) - abs(z)) < abs(depth[1])):
                # this happens, if a small amount is the rest
                z -= (abs(depth[0]) - abs(z))
                print "rest Z: {}".format(z)
            else:
                z -= abs(depth[1])
                print "new Z: {}".format(z)

            loop += CR
            gc += spaces + "(-- START Track Loop  --)" + CR
            for t in pocketMillTracks:
                # every track contain a fixed number of separate gCode
                # commands
                spaces2 = spaces.ljust(2)
                # set new depth
                gc += CR + spaces2 + "(-- next depth z {0:08.3f} --){1}".format(
                    z, CR)
                gc += spaces2 + "G01 Z{0:08.3f} {1}".format(z, CR)
                for cmd in t:
                    #
                    # combine all parameter to one command
                    gc += spaces2
                    #  0  1  2  3  4
                    # GC, X, Y, I, J
                    print cmd
                    for p in range(len(cmd)):
                        if p == 0:
                            gc += cmd[p]
                        if p == 1:
                            f = " F{0:05.1f}".format(float(cmd[p]))
                        if p == 2:
                            gc += " X{0:08.3f}".format(float(cmd[p]))
                        if p == 3:
                            gc += " Y{0:08.3f}".format(float(cmd[p]))
                        if p == 4:
                            gc += " I{0:08.3f}".format(float(cmd[p]))
                        if p == 5:
                            gc += " J{0:08.3f}".format(float(cmd[p]))

                    gc += f + CR

            gc += spaces + "(-- END Track Loop  --)" + CR
            pass

        gc += "(-- END DEPTH loop --)" + CR
        gc += self.getGCode_Homeing(cPoint[0], cPoint[1], zPos["safetyZ"],
                                    feeds["XYG0"])
        gc += self.getGCode_Postamble()
        gc += CR
        return gc

    def __createPocketTracks(self, cPoint, sizeAB, r, feeds, offset=0.0):
        '''
        This method create for a track all needed GCode parameters and save
        them in a list. This list is used (afterwards) to create the real
        GCode commands

        This method is called in a loop with a new offset. The offset describes
        next millings position
        '''
        # h = h1 + 2*r
        # w = w1 + 2*r
        w0 = sizeAB[1]
        w1 = sizeAB[1] - (2 * r)  # horizontal distance between arcs
        h0 = sizeAB[0]
        h1 = sizeAB[0] - (2 * r)  # vertical distance betwween arcs

        x = cPoint[0]
        y = cPoint[1]
        # sequence to mill a rounded rectangle
        seq = [
            #start
            ("G01", feeds["XYGn"], x, y - offset),
            # arc1
            # G02, F X Y I J
            ("G02", feeds["XYGn"], x - r - offset, y + r, 0.0, r + offset),
            # vertical to arc2
            ("G01", feeds["XYGn"], x - r - offset, y + r + h1),
            # arc2
            # G02, F X Y I J
            ("G02", feeds["XYGn"], x, y + h0 + offset, r + offset, 0.0),
            # horizontal to arc 3
            ("G01", feeds["XYGn"], x + w1, y + h0 + offset),
            # arc 3
            # G02, F X Y I J
            ("G02", feeds["XYGn"], x + w1 + r + offset, y + r + h1, 0.0,
             -r - offset),
            # vertical to arc 4
            ("G01", feeds["XYGn"], x + w1 + r + offset, y + r),
            # arc 4
            # G02, G02, F X Y I J
            ("G02", feeds["XYGn"], x + w1, y - offset, -r - offset, 0.0),
            # go back to start position
            ("G01", feeds["XYGn"], x, y - offset),
        ]
        #print "{1}---- offset {0} -----".format(offset,CR)
        #print seq
        return seq
