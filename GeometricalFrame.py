from Tkinter import *
from tkFont import Font
from math import *
from tkFont import Font
from math import *
from tkSimpleDialog import *
import tkMessageBox


CR = '\n'

class GeometricalFrame(Frame):
    def __init__(self, app, master, frame, title):
        self.app = app
        self.parentFrame = frame
        self.title = title
        self.master = master
        self.master.geometry("800x700")
        self.app.master.title(title)
        self.frmButtonsIndividualContent = Frame(self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)

    def show(self):
        print "Show"
        self.__frmImage()
        self.__frmStandardContent()
        self._frmIndividualContent()
        self.__buttonBox()
        pass

    def __frmImage(self):
        print "__frmImage"
        self.frmImage = Frame(self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)
        self.frmImage.grid(row=0,column=0, rowspan=5)
        self.frmImage.pack(expand=True)
        pass

    def __frmStandardContent(self):
        print "__frmStandardContent"
        self.frmStandardContent = Frame(self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)
        row = 0
        self._preamble = StringVar()
        self._preamble.set("G21 G90 G64 G17 G40 G49")
        Label(self.frmStandardContent, text="PreGCode").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmStandardContent, width=70, mandatory=False,
            textvariable=self._preamble).grid(row=row, column=1, sticky=W)

        row += 1
        self._postamble = StringVar()
        post = "G00 Z10 F100 \n"
        post+= "M2"
        self._postamble.set(post)
        Label(self.frmStandardContent, text="PostGCode").grid(row=row, column=0, sticky=W)
        FloatEntry(self.frmStandardContent, width=70, mandatory=False,
            textvariable=self._postamble).grid(row=row, column=1, sticky=W)

        self.frmStandardContent.pack(expand=True, fill=BOTH)
        pass

    def _frmIndividualContent(self):
        #override in subcluss
        pass

    def __buttonBox(self):
        print "__buttonBox"
        self.frmButtons = Frame(self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)

        btnAxis = Button(self.frmButtons, text="To AXIS", width=10,
            command=self.copyAXIS, default=ACTIVE).grid(
                row=0, column=0
            )

        btnClip = Button(self.frmButtons, text="To Clipboard", width=10,
            command=self.copyClipboard).grid(
                row=0, column=1
            )

        btnOK = Button(self.frmButtons, text="Gcode", width=10,
            command=self.showGCode).grid(
                row=0, column=2
            )

        btnCancel = Button(self.frmButtons, text="Cancel", width=10,
            command=self.cancel).grid(
                row=0, column=3
            )


        #self.bind("<Return>", self.copyAXIS)
        #self.bind("<Escape>", self.cancel)
        #self.bind("<Button-1>", self.copyClipboard)

        self.frmButtons.pack(expand=True, fill=BOTH)

    def generateGCode(self):
        # override from subclass
        pass

    def copyClipboard(self, event=None):
        print "copyClipboard"
        self.app.clipboard_clear()
        self.app.clipboard_append(self.getGCode())
        pass

    def saveFile(self, event=None):
        print "saveFile"
        pass

    def copyAXIS(self, event=None):
        gc = self.getGCode()
        print "copyAXIS ({})".format(gc)
        sys.stdout.write(self.getGCode())
        self.quit()

    def showGCode(self, event=None):
        gc = self.getGCode()
        print ">> call d.setData({})".format(gc)
        d = GCodeDialog(self.app, title="generated GCode")
        d.init(gc)
        d.update(gc)
        pass

    def getGCode(self):
        gc = "%"
        gc += '''
(--------------------------)
(          __              )
(  _(\    |@@|             )
( (__/\__ \--/ __          )
(    \___|----|  |   __    )
(        \ }{ /\ )_ / _\\  )
(        /\__/\ \__O (__   )
(       (--/\--)    \__/   )
(       _)(  )(_           )
(      `---''---`          )
(    (c) by LunaX 2018     )
(--------------------------)
        '''
        gc += CR
        gc += self.generateGCode()
        gc += "%" + CR
        return gc

    #------ EXIT --------------------------
    def cancel(self, event=None):
        print "cancel"
        self.master.quit()
        pass

    def MessageBox(self, state="INFO", title = "", text=""):
        if state == "INFO":
            tkMessageBox.showinfo(title, text)
        elif state == "WARN":
            tkMessageBox.showinfo(title, text)
        elif state == "ERROR":
            tkMessageBox.showerror(title, text)
        else:
            tkMessageBox.showtitle("!!!unknown - State !!!", text)
