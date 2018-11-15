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
class SurfaceRectangle(GeometricalFrame):

    #
    # define your own images to describe your GCode-Generator
    def init(self):
        self.__imageNames = [
            # left down
            "./img/surface/zigzag_X_001.png"
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
        #choices = [1]
        choices = [1]

        self.__CC = StringVar()
        self.__CC.set(choices[0])
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
        self.__tooldia = StringVar(value="6.0")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        w6 = FloatEntry(self.frmButtonsIndividualContent, width=5, mandatory=False,
            textvariable=self.__tooldia)
        w6.grid(row=row, column=1, sticky=W)
        w6.focus()

        #
        # stepover from row to row
        row += 1
        self.__stepover = StringVar(value="80")
        Label(self.frmButtonsIndividualContent, text="Stepover tooldia %").grid(
            row=row, column=0, sticky=W)
        w7 = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__stepover, mandatory=False)
        w7.grid(
            row=row, column=1, sticky=W)
        ToolTip(w7,text="This percentage is the overlap from row to row based on tool diameter. Normally the value should be between 30-90%")

        self.__overshot = StringVar(value="110")
        Label(self.frmButtonsIndividualContent, text="Overshot %").grid(
            row=row, column=2, sticky=W)
        w7a = FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__overshot, mandatory=False)
        w7a.grid(
            row=row, column=3, sticky=W)
        ToolTip(w7a,
        text='''This percentage is an overshot for used tool on work piece edges. Normally the value should be between 0-150%. Values >= 100 move tool completely outside from work piece''')

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
        self.__distanceA = StringVar(value="70.0")
        self.__distanceB = StringVar(value="100.0")
        Label(self.frmButtonsIndividualContent, text="Height (a)").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Width (b)").grid(row=row, column=2, sticky=W)
        w8 = FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__distanceA)
        w8.grid(row=row, column=1, sticky=W)
        w9 = FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__distanceB)
        w9.grid(row=row, column=3, sticky=W)
        ToolTip(w8,text="length of work piece")
        ToolTip(w9,text="width of work piece")

        row += 1
        self.__depthtotal = StringVar(value="-1.0")
        self.__depthstep = StringVar(value="-0.2")
        Label(self.frmButtonsIndividualContent, text="Total depth").grid(row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="depth cutting per step").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__depthtotal, mandatory=True).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
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
        a = float(self.__distanceA.get())
        b = float(self.__distanceB.get())
        toolDia = float(self.__tooldia.get())
        stepover = float(self.__stepover.get())
        overshot = float(self.__overshot.get())

        if (a <= 0.0 or b <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="a and b should be greater than 0.0")
            return False

        if (toolDia <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tool diamater should be greater than 0.0")
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
        sizeAB = (float(self.__distanceA.get()),
                  float(self.__distanceB.get()))
        toolDia = float(self.__tooldia.get())

        pWidth = sizeAB[1]
        stepover = float(self.__stepover.get())
        overshot = float(self.__overshot.get())
        orientation = 1

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
        # This loop asume, that you try to mill into your object.
        # if not needed for your shape, remove this part and rewrite
        #----------------------------------------------------------------------
        #

        offset = toolDia / 2.0
        cWidth = 0.0             # start pocket width = tool diameter
        pocketMillTracks = []
        x = 1
        finished = False
        #
        # set to left down corner
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            cPoint[0],
            cPoint[1],
            feeds["XYG0"],
            CR)
        while (not finished):
            if (cWidth > sizeAB[1]) :
                 finished = True

            t, cPoint, yOff = self.__createPocketTracks(
                cPoint,
                sizeAB,
                toolDia,
                feeds,
                orientation,
                stepover,
                overshot

            )

            pocketMillTracks.append(t)
            x += 1
            cWidth += yOff
            pass

        #
        # it's time to generate the real gCode
        #
        # Every round we mill all tracks in the same detph
        # than we increase depth as long as we reached total depthStep

        gc += CR + "(-- START DEPTH Loop --)" + CR
        z = 0.0
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
                gc += CR + spaces2 + "(-- next depth z {0:08.3f} --){1}".format(z,CR)
                for cmd in t:
                    #
                    # combine all parameter to one command
                    gc += spaces2
                    print cmd
                    #
                    # pattern to recognize special command set
                    regFloat = r"{\d:\d+\.\d+f}"
                    for p in range(len(cmd)):
                        if isinstance(cmd[p], basestring):
                            x = re.findall(regFloat,cmd[p], re.UNICODE)
                            if (len(x) != 0):
                                #print "RegFloat found"
                                gc += cmd[p].format(float(z))
                            else:
                                # normal string
                                gc += " " + cmd[p]
                        if isinstance(cmd[p], float):
                            gc += "{0:08.3f}".format(cmd[p])
                        if isinstance(cmd[p], int):
                            gc += "{0:05d}".format(cmd[p])
                    gc += CR

            gc += spaces + "(-- END Track Loop  --)" + CR
            pass

        gc += "(-- END DEPTH loop --)" + CR
        gc += self.getGCode_Homeing(
            cPoint[0],
            cPoint[1],
            zPos["safetyZ"],
            feeds["XYG0"]
        )
        gc += self._postamble.get() + CR
        gc += CR
        return  gc

    def __createPocketTracks(self, cPoint, sizeAB, toolDia, feeds,
                            orientation=1, stepover=80, overshot=110 ):
        '''
        This method create for a track all needed GCode parameters and save
        them in a list. This list is used (afterwards) to create the real
        GCode commands

        This method is called in a loop with a new offset. The offset describes
        next millings position

        parameters
        cPoint          base position for X/Y
        sizeAB          widht, length (a + b)
        tollDia         diameter of used tool
        orientation     1 = from left to right than up (default)
                        2 = from right to left than up
                        3 = from down to up than right
                        4 = from down to up than left
        Stepover        percentage of tooldia (default 80%)
        '''
        #r = toolDia / 2.0
        offsetStepover = float(toolDia - (toolDia * stepover / 100.0))
        offsetOvershot = float(toolDia * overshot / 100) - float(toolDia / 2.0)

        a = sizeAB[0]   # widht
        b = sizeAB[1]   # height
        # definition w = width is size of work piece in X-direction (=> a) + overshot
        # definition h = height is size of work piece in Y-Direction (=> b) + overshot
        w = a + (offsetOvershot*2)
        h = b + (offsetOvershot*2)

        x = cPoint[0]  # we assume, that cp is left down edge
        y = cPoint[1]  # dito

        # this temp variables are used to set real x/y postion based on orientation
        # if values are
        # xStepOver positiv move from left to right
        # xStepOver negativ move from right to left
        # yStepOver positiv move from down to up
        # yStepOver negativ move from up to down

        xStepOver = yStepOver = 0.0
        if orientation == 1:
            # cp is at left down edge
            x -= offsetOvershot
            yStepOver = offsetStepover  # move up
        elif orientation == 2:
            # cp is at right down edge
            x += (a + offsetOvershot)
            w *= -1 # move from right to left
            yStepOver = offsetStepover  # move up
        elif orientation == 3:
            # cp is at left upper edge
            x -= offsetOvershot
            y += b
            yStepOver = -offsetStepover # move down
            h *= -1
        elif orientation == 4:
            x += (a + offsetOvershot)
            y += b
            yStepOver = -offsetStepover # move down
            h *= -1
            w *= -1


        print "a {} b {} x {} y {} w {} h {} overshot {} stepover {} xStepOver {} yStepOver {} ".format(
            a,b, x, y, w, h, offsetOvershot, offsetStepover, xStepOver, yStepOver
        )

        # sequence to mill a rounded rectangle
        seq = [
            #start
            # go to depth
            ("G01", "Z", "{0:08.3f}", "F", feeds["ZGn"], ),
            # move to start position
            ("G01", "X", x, "Y", y, "F", feeds["XYGn"], ),
            # move to next horizontal position
            ("G01", "X", x + w , "Y", y, "F", feeds["XYGn"], ),
            # move next Y position
            ("G01", "X", x + w , "Y", y + yStepOver, "F", feeds["XYGn"], ),
            # move next horizontal position
            ("G01", "X", x, "Y", y + yStepOver, "F", feeds["XYGn"], ),
        ]
        # set new start position
        cPoint = (
            cPoint[0],
            cPoint[1] + yStepOver
        )
        return seq, cPoint, yStepOver
