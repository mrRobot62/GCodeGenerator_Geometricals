'''
    Geometical class

    This class generate G-Code for Arcs
'''

from tkSimpleDialog import *
from Tkinter import *
from tkFont import Font
from math import *
from PIL import Image, ImageTk
import tkMessageBox
import os

CR = "\n"


class ClassContourArc(Dialog):

    def radioImageCallback(self):
        p = self.path[int(self.__CC.get())-1]
        self.img = Image.open(p)
        self.photo = ImageTk.PhotoImage(self.img)
        Label(self.master, image=self.photo).grid(
            row=0, column=0, sticky=W+E+N+S, columnspan=2
        )

    def body(self, master):
        self.master = master
        self.path = [
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

        row = 1
        self.__CC = StringVar()
        self.__CC.set("5")
        self.radioImageCallback()
        Label(master, text='Coordinate Center').grid(row=row, column=0, sticky=W)
        Radiobutton(master, text="1", variable=self.__CC,
                    value=1, command=self.radioImageCallback).grid(row=row, column=1, sticky=W)
        Radiobutton(master, text="2", variable=self.__CC,
                    value=2, command=self.radioImageCallback).grid(row=row, column=2, sticky=W)
        Radiobutton(master, text="3", variable=self.__CC,
                    value=3, command=self.radioImageCallback).grid(row=row, column=3, sticky=W)
        Radiobutton(master, text="4", variable=self.__CC,
                    value=4, command=self.radioImageCallback).grid(row=row, column=4, sticky=W)
        Radiobutton(master, text="5", variable=self.__CC,
                    value=5, command=self.radioImageCallback).grid(row=row, column=5, sticky=W)

        row = row+1
        self.__unit = StringVar()
        self.__unit.set("G21")
        Label(master, text='Unit').grid(row=row, column=0, sticky=W)
        Radiobutton(master, text="mm", variable=self.__unit,
                    value="G21").grid(row=row, column=1, sticky=W)
        Radiobutton(master, text="inch", variable=self.__unit,
                    value="G20").grid(row=row, column=2, sticky=W)

        row = row + 1
        self.__dir = StringVar()
        self.__dir.set("G02")
        Label(master, text='Contour direction').grid(
            row=row, column=0, sticky=W)
        Radiobutton(master, text="CW (G02)", variable=self.__dir,
                    value="G02").grid(row=row, column=1, sticky=W)
        Radiobutton(master, text="CCW (G03)", variable=self.__dir,
                    value=1).grid(row=row, column=2, sticky=W)

        row = row + 1
        self.__cuttercompensation = StringVar()
        self.__cuttercompensation.set("G40")
        Label(master, text='Tool movement').grid(row=row, column=0, sticky=W)
        Radiobutton(master, text="on contour", variable=self.__cuttercompensation,
            value="G40").grid(row=row, column=1, sticky=W)
        Radiobutton(master, text="left from contour", variable=self.__cuttercompensation,
            value="G41").grid(row=row, column=2, sticky=W)
        Radiobutton(master, text="right from contour", variable=self.__cuttercompensation,
            value="G42").grid(row=row, column=3, sticky=W)

        row = row + 1
        self.__preamble = StringVar()
        preamble = "G21 G90 G64 G17 G40 G49"
        Label(master, text="Preamble:").grid(row=row, column=0, sticky=W)
        FloatEntry(master, width=60, mandatory=False, value=preamble,
            textvariable=self.__preamble).grid(row=row, column=1, columnspan=3, sticky=W)

        row = row + 1
        self.__tooldia = StringVar()
        Label(master, text="Tool diameter:").grid(row=row, column=0, sticky=W)
        FloatEntry(master, width=10, value="3.0", mandatory=False,
            textvariable=self.__tooldia).grid(row=row, column=1, sticky=W)

        row = row + 1
        self.__centerX = StringVar()
        self.__centerY = StringVar()
        Label(master, text='Center X:*').grid(row=row, column=0, sticky=W)
        Label(master, text="Center Y:*").grid(row=row, column=2, sticky=W)
        FloatEntry(master, width=10, value="0.0", mandatory=True,
            textvariable=self.__centerX).grid(row=row, column=1, sticky=W)
        FloatEntry(master, width=10, value="0.0", mandatory=True,
            textvariable=self.__centerY).grid(row=row, column=3, sticky=W)

        row = row + 1
        self.__dia = StringVar()
        Label(master, text="Arc diameter:*").grid(row=row, column=0, sticky=W)
        FloatEntry(master, width=10, value = "", mandatory=True,
            textvariable=self.__dia,
            background="Red").grid(row=row, column=1, sticky=W)

        row = row + 1
        self.__arcstart = StringVar()
        self.__arcend = StringVar()
        Label(master, text="Start arc(0-360):").grid(row=row, column=0, sticky=W)
        Label(master, text="End arc (0-360):").grid(row=row, column=2, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__arcstart).grid(
            row=row, column=1, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__arcend).grid(row=row, column=3, sticky=W)

        row = row + 1
        self.__depthtotal = StringVar()
        self.__depthstep = StringVar()
        Label(master, text="Total depth:*").grid(row=row, column=0, sticky=W)
        Label(master, text="depth cutting per step:*").grid(
            row=row, column=2, sticky=W)
        FloatEntry(master, width=5, value="0.5",
            textvariable=self.__depthtotal, mandatory=True).grid(
            row=row, column=1, sticky=W)
        FloatEntry(master, width=5, value="0.5",
            textvariable=self.__depthstep, mandatory=True).grid(
            row=row, column=3, sticky=W)

        row = row + 1
        self.__speed_XY_G00 = StringVar()
        self.__speed_Z_G00 = StringVar()
        Label(master, text="Feed (G00 X/Y):").grid(row=row, column=0, sticky=W)
        Label(master, text="Feed (G00 Z):").grid(row=row, column=2, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_XY_G00, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_Z_G00, mandatory=False).grid(row=row, column=3, sticky=W)

        row = row + 1
        self.__speed_XY_G02G03 = StringVar()
        self.__speed_Z_G01 = StringVar()
        Label(master, text="Feed (G02/G03 X/Y):").grid(row=row, column=0, sticky=W)
        Label(master, text="Feed (G01 Z):").grid(row=row, column=2, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_XY_G02G03, mandatory=False).grid(
            row=row, column=1, sticky=W)
        FloatEntry(master, width=5, value="0.0",
            textvariable=self.__speed_Z_G01, mandatory=False).grid(
            row=row, column=3, sticky=W)

        row = row + 1
        self.__start_Z = StringVar()
        Label(master, text="Start Z:").grid(row=row, column=0, sticky=W)
        FloatEntry(master, width=10, value="3.0",
            textvariable=self.__start_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)

        row = row + 1
        self.__safety_Z = StringVar()
        Label(master, text="Safety Z:").grid(row=row, column=0, sticky=W)
        FloatEntry(master, width=10, value="10.0",
            textvariable=self.__safety_Z, mandatory=False).grid(
            row=row, column=1, sticky=W)
        return None

    def apply(self):
        gc = ""
        # Preamble
        gc += CR + "(set countour arc preamble)" + CR
        gc += self.__preamble.get() + CR
        # set Unit
        gc += self.__unit.get() + CR
        # set Z axis
        gc += CR + "(set Z saftey position)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__safety_Z.get()),
            float(self.__speed_Z_G00.get()), CR)

        xoffset = 0.0
        yoffset = 0.0
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
            xoffset = 0 # ignore user input
            yoffset = 0 # ignore user input
        # X
        X = (float(self.__dia.get()) / 2.0) + xoffset

        # y
        Y = float(self.__centerY.get()) + yoffset

        # I - this is the radius
        I = (float(self.__dia.get()) / 2.0) * -1.0

        # J
        J = -0.0

        # cutter compensation
        if (self.__cuttercompensation.get() == "G40"):
            gc += CR + "(-- Cutter compensation --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
        if (self.__cuttercompensation.get() == "G41"):
            gc += CR + "(-- Cutter compensation LEFT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
            X -= (float(self.__tooldia) / 2.0)
        if (self.__cuttercompensation.get() == "G41"):
            gc += CR + "(-- Cutter compensation RIGHT --){}".format(CR)
            gc += "{} {}".format(self.__cuttercompensation.get(),CR)
            X += (float(self.__tooldia) / 2.0)

        # set start postion X/Y
        gc += "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}".format(
            float(X),
            float(Y),
            float(self.__speed_XY_G00.get()),
            CR)

        # start with circel
        gc += CR + "(move Z-axis to start postion near surface)" + CR
        gc += "G00 Z{0:08.3f} F{1:05.1f} {2}".format(
            float(self.__start_Z.get()),
            float(self.__speed_Z_G00.get()), CR)
        #
        # generate as many circle steps as needed until depthtotal is reached
        # cut an Arc
        step = float(self.__depthstep.get())
        depth = float(self.__depthtotal.get())
        z = 0.0
        loop = ""
        gc += CR + "(------- start circel -------------)" + CR
        gc += "(-- Dia {0:06.3f}, Depth {1:06.3f}, Step Z {2:06.3f} --){3}".format(
            float(self.__dia.get()),
            depth,
            step,
            CR
        )
        gc += "(-- X {0:06.3f}, Y {1:06.3f} --) {}".format(
            float(X),
            float(Y),
            CR
        )
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
                float(z),
                float(self.__speed_Z_G01.get()), CR)
            # set direction G02/G03
            #
            loop += self.__dir.get()
            loop += " X{0:08.3f} Y{1:08.3f} I{2:08.3f} J{3:08.3f} F{4:05.1f} {5}".format(
                X, Y, I, J, float(self.__speed_XY_G02G03.get()), CR
            )
            #
            # for saftey issues.
            if (abs(step) == 0.0):
                break

        gc += loop
        #----------------------------
        gc += "(----------------------------------)" + CR
        gc += "M02 (program end)" + CR
        gc += CR
        print gc
        self.result = gc
