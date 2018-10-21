from Tkinter import *
from tkFont import Font
from math import *
from tkFont import Font
from math import *
from tkSimpleDialog import *
import tkMessageBox
import tkFileDialog

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
        self.setBtnStates(state=NORMAL)
        pass

    def onClose(self):
        """ """
        self.destroy()
        self.original_frame.show()

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

        self.btnAxis = Button(self.frmButtons, text="To AXIS", width=10,
            command=self.copyAXIS, state=DISABLED)
        self.btnAxis.grid(
                row=0, column=0
            )

        self.btnClip = Button(self.frmButtons, text="To Clipboard", width=10,
            command=self.copyClipboard, state=DISABLED)
        self.btnClip.grid(
                row=0, column=1
            )

        self.btnSave = Button(self.frmButtons, text="Save as", width=10,
            command=self.saveFile, state=DISABLED)
        self.btnSave.grid(
                row=0, column=2
            )

        self.btnGCode = Button(self.frmButtons, text="Gcode", width=10,
            command=self.showGCode, state=DISABLED)
        self.btnGCode.grid(
                row=0, column=3
            )

        self.btnCancel = Button(self.frmButtons, text="Cancel", width=10,
            command=self.cancel, state=NORMAL)
        self.btnCancel.grid(
                row=0, column=4
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
        gc = self.getGCode()
        if gc is None:
            return None
        self.app.clipboard_clear()
        self.app.clipboard_append(gc)
        pass

    def saveFile(self, event=None):
        gc = self.getGCode()
        if gc is None:
            return None
        fname = tkFileDialog.asksaveasfilename(
            initialdir = "./",
            title = "Save file",
            defaultextension = "*.ngc",
            filetypes = (("Axis ","*.ngc"),("Gcode ","*.gc"),("all files","*.*"))
            )
        if (fname == None):
            # cancle button
            return None
        print ("Save gcode to '{}'".format(fname))
        f = open(fname,"w")
        f.write(gc)
        f.close()
        pass

    def copyAXIS(self, event=None):
        print ("copyAXIS")
        gc = self.getGCode()
        if gc is None:
            return None
        sys.stdout.write(self.getGCode())
        self.quit()

    def showGCode(self, event=None):
        gc = self.getGCode()
        if gc is None:
            return None
        d = GCodeDialog(self.app, title="generated GCode")
        d.init(gc)
        d.update(gc)
        pass

    def setBtnStates(self, state):
        self.btnClip.config(state=state)
        self.btnSave.config(state=state)
        self.btnAxis.config(state=state, default=ACTIVE)
        self.btnGCode.config(state=state)

    def userInputValidation(self):
        # override in subclass
        '''
        This function is called from getGCode() and validate all important
        input fields in the current dialog.
        Implementation should be done inside subclass

        This method should return True or False
            True if everything is ok
            False something is wrong - no GCode generation
        '''
        pass

    def getGCode(self):
        if self.userInputValidation() == False:
            return None
        gc = "%"
        gc += '''
(--------------------------)
(          __              )
(  _(\    |@@|             )
( (__/\__ \--/ __          )
(    \___|----|  |   __    )
(        \ }{ /\ )_ / _\   )
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
        self.destroy()
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
