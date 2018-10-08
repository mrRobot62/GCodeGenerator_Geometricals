'''
    Geometical template file

    This class generate G-Code for xxx
'''

from tkSimpleDialog import *
from Tkinter import *
from tkFont import Font
from math import *
from PIL import Image, ImageTk
import tkMessageBox
import os

CR = "\n"

#
# change class name into a "usable name" like ClassContourRect
class ClassShapeDefinition(Dialog):

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
            "./img/contour/circle-pic1_4.jpg
            ",
            # center
            "./img/contour/circle-pic1_5.jpg"
        ]

        row = 1
        self.__CC = StringVar()
        self.__CC.set("5")
        Label(master, text='Coordinate Center').grid(row=row, column=0, sticky=W)
        Radiobutton(master, text="1", variable=self.__CC,
                    value="1", command=self.radioImageCallback).grid(row=row, column=1, sticky=W)
        Radiobutton(master, text="2", variable=self.__CC,
                    value="2", command=self.radioImageCallback).grid(row=row, column=2, sticky=W)
        Radiobutton(master, text="3", variable=self.__CC,
                    value="3", command=self.radioImageCallback).grid(row=row, column=3, sticky=W)
        Radiobutton(master, text="4", variable=self.__CC,
                    value="4", command=self.radioImageCallback).grid(row=row, column=4, sticky=W)
        Radiobutton(master, text="5", variable=self.__CC,
                    value="5", command=self.radioImageCallback).grid(row=row, column=5, sticky=W)
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

        #------- insert your individual widgets here ---------------------

        #-----------------------------------------------------------------

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
        gc = "%"
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

        #--------------------------------------------------------------
        #   start individual gcode
        #--------------------------------------------------------------


        #--------------------------------------------------------------
        #   end individual gcode
        #--------------------------------------------------------------
        #----------------------------
        gc += "(----------------------------------)" + CR
        gc += "G00 Z{0:08.3f} Y{1:08.3f} {2}".format(
        self.__safety_Z, CR)
        gc += "G00 X{0:08.3f} Y{1:08.3f} {2}".format(
            self.__centerX.get(), self.__centerY.get(),CR)
        gc += "M02 (program end)" + CR
        gc += "(----------------------------------)" + CR
        gc += "%" + CR
        #print gc
        self.result = gc
