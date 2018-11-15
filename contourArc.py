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



class ContourArc(GeometricalFrame):

    def init(self):
        self.__imageNames = [
            # left down
            "./img/contour/circle-pic1_1.jpg",
            # left upper
            "./img/contour/circle-pic1_2.jpg",
            # right upper
            "./img/contour/circle-pic1_3.jpg",
            # right down
            "./img/contour/circle-pic1_4.jpg",
            # center
            "./img/contour/circle-pic1_5.jpg"
        ]

    def _changeImage(self):
        print len(self.__imageNames)
        p = self.__imageNames[int(self.__CC.get())-1]
        self.img = PIL.Image.open(p)
        self.photo = PIL.ImageTk.PhotoImage(self.img)
        Label(self.frmImage, image=self.photo).grid(
            row=0, column=0, sticky=W+E+N+S, columnspan=2
        )

    def _frmIndividualContent(self):
        self.init()
        row = 0
        self.__CC = StringVar()
        self.__CC.set("5")
        self._changeImage()
        Label(self.frmButtonsIndividualContent, text='Coordinate Center').grid(row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="1", variable=self.__CC,
                    value=1, command=self._changeImage).grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="2", variable=self.__CC,
                    value=2, command=self._changeImage).grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="3", variable=self.__CC,
                    value=3, command=self._changeImage).grid(row=row, column=3, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="4", variable=self.__CC,
                    value=4, command=self._changeImage).grid(row=row, column=4, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="5", variable=self.__CC,
                    value=5, command=self._changeImage).grid(row=row, column=5, sticky=W)

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
        self.__cuttercompensation.set("G40")
        Label(self.frmButtonsIndividualContent, text='Tool movement').grid(
            row=row, column=0, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="on contour", variable=self.__cuttercompensation,
            value="G40").grid(row=row, column=1, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="left from contour", variable=self.__cuttercompensation,
            value="G41").grid(row=row, column=2, sticky=W)
        Radiobutton(self.frmButtonsIndividualContent, text="right from contour", variable=self.__cuttercompensation,
            value="G42").grid(row=row, column=3, sticky=W)

        row += 1
        self.__tooldia = StringVar(value="3.0")
        Label(self.frmButtonsIndividualContent, text="Tool diameter").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)

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
        self.__dia = StringVar()
        Label(self.frmButtonsIndividualContent, text="Arc diameter").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10, mandatory=True,
            textvariable=self.__dia,
            vcmd=self.__validation,
            background="Red").grid(row=row, column=1, sticky=W)

        row += 1
        self.__arcstart = StringVar(value="0.0")
        self.__arcend = StringVar(value="0.0")
        Label(self.frmButtonsIndividualContent, text="Start arc(0-360)").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="End arc (0-360)").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__arcstart).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__arcend).grid(row=row, column=3, sticky=W)

        row += 1
        self.__depthtotal = StringVar(value="-0.5")
        self.__depthstep = StringVar(value="-0.5")
        Label(self.frmButtonsIndividualContent, text="Total depth").grid(
            row=row, column=0, sticky=W)
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
        Label(self.frmButtonsIndividualContent, text="Feed (G00 X/Y)").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G00 Z)").grid(
            row=row, column=2, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_XY_G00, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=5,
            textvariable=self.__speed_Z_G00, mandatory=False).grid(
                row=row, column=3, sticky=W)

        row += 1
        self.__speed_XY_G02G03 = StringVar(value="100.0")
        self.__speed_Z_G01 = StringVar(value="80.0")
        Label(self.frmButtonsIndividualContent, text="Feed (G02/G03 X/Y)").grid(
            row=row, column=0, sticky=W)
        Label(self.frmButtonsIndividualContent, text="Feed (G01 Z)").grid(
            row=row, column=2, sticky=W)
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
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__start_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)

        row += 1
        self.__safety_Z = StringVar(value="10.0")
        Label(self.frmButtonsIndividualContent, text="Safety Z").grid(
            row=row, column=0, sticky=W)
        FloatEntry(self.frmButtonsIndividualContent, width=10,
            textvariable=self.__safety_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)

        #-----------------------------------------------------
        self.frmButtonsIndividualContent.pack(expand=True, fill=BOTH)
        pass

    def __validation(self, nV, **kv):
        # nothing
        return True

    def userInputValidation(self):
        if (self.__dia.get() is None or
            self.__dia.get() == "" or
            float(self.__dia.get()) <= 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Diameter should be greater than 0.0")
            return False

        if (float(self.__tooldia.get()) >= float(self.__dia.get())):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Tooldiamter should be less than arc diameter")
            return False

        if (float(self.__centerX.get()) < 0.0 or float(self.__centerY.get()) < 0.0):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Values for CenterX/Y should be positive")
            return False


        if (float(self.__arcstart.get()) > float(self.__arcend.get())):
            self.MessageBox(state="ERROR",
                title="ERROR",
                text="Arc-Start should be less than Arc-End")
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

    def generateGCode(self):
        gc = ""
        # Preamble
        gc += CR + "(set countour arc preamble)" + CR
        gc += self._preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        toolDia = float(self.__tooldia.get())

        X = xoffset = float(0.0)
        Y = yoffset = float(0.0)
        if (int(self.__CC.get()) == 1):
            xoffset = float(self.__centerX.get())
            yoffset = float(self.__centerY.get())
        if (int(self.__CC.get()) == 2):
            xoffset = float(self.__centerX.get())
            yoffset = -float(self.__centerY.get())
        if (int(self.__CC.get()) == 3):
            xoffset = -float(self.__centerX.get())
            yoffset = -float(self.__centerY.get())
        if (int(self.__CC.get()) == 4):
            xoffset = -float(self.__centerX.get())
            yoffset = float(self.__centerY.get())
        if (int(self.__CC.get()) == 5):
            xoffset = float(0.0) # ignore user input
            yoffset = float(0.0) # ignore user input

        intend = "".ljust(2)
        # X
        #X = (float(self.__dia.get()) / 2.0) + xoffset
        X += xoffset
        # Y
        #Y = float(self.__centerY.get()) + yoffset
        Y += yoffset

        # I - this is the radius
        R = (float(self.__dia.get()) / 2.0)
        I = R * -1.0


        # J
        J = -0.0

        # set start postion X/Y
        # for milling an arc, we move to 3clock position and start from
        # this position
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            float(X+R),
            float(Y),
            float(self.__speed_XY_G00.get()),
            CR)

        # start with circel
        gc += CR + "(move Z-axis to start postion near surface)" + CR
        gc += "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__start_Z.get()),
            float(self.__speed_Z_G01.get()), CR)
        #
        # generate as many circle steps as needed until depthtotal is reached
        # cut an Arc
        step = float(self.__depthstep.get())
        depth = float(self.__depthtotal.get())
        z = 0.0
        loop = ""
        gc += CR + "(-- START circel --)" + CR
        gc += "(-- Dia {0:06.3f}, Depth {1:06.3f}, Step Z {2:06.3f} --){3}".format(
            float(self.__dia.get()),
            depth,
            step,
            CR
        )
        gc += "(-- X {0:06.3f}, Y {1:06.3f} --) {2}".format(
            float(X+R),
            float(Y),
            CR
        )
        gc += "(-- LOOP --)" + CR + CR
        # cutter compensation
        #
        gc += self.getGCodeCutterComp(
            self.__cuttercompensation.get(),
            toolDia
        )
        while (abs(z) < abs(depth)):
            # set next Z depth
            if ((abs(depth) - abs(z)) < abs(step)):
                # this happens, if a small amount is the rest
                z -= (abs(depth) - abs(z))
                print "rest Z: {}".format(z)
            else:
                z -= abs(step)
                print "new Z: {}".format(z)

            loop += intend + "(set new Z {0:05.2f} position)".format(z) + CR
            loop += intend + "G01 Z{0:08.3f} F{1:05.1f} {2}".format(
                float(z),
                float(self.__speed_Z_G01.get()), CR)
            # set direction G02/G03
            #
            loop += intend + self.__dir.get()
            loop += " X{0:08.3f} Y{1:08.3f} I{2:08.3f} J{3:08.3f} F{4:05.1f} {5}".format(
                X+R, Y, I, J, float(self.__speed_XY_G02G03.get()), CR
            )
            loop += CR
            #
            # for saftey issues.
            if (abs(step) == 0.0):
                break
            pass

        gc += loop
        #----------------------------
        gc += CR + "(-- END circle -)" + CR
        gc += self.getGCode_Homeing(
            X,Y,
            float(self.__safety_Z.get()),
            float(self.__speed_XY_G00.get()),
            float(self.__speed_Z_G00.get())
        ) + CR
        gc += self._postamble.get() + CR
        gc += CR
#        print gc
        return  gc
