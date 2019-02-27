from Tkinter import *
from tkFont import Font
from math import *
from tkFont import Font
from math import *
from tkSimpleDialog import *
import tkMessageBox
import tkFileDialog
import re
import ttk
import json

CR = '\n'

# Bugfix 25.02.2019 - on MacOS with MOJAVE there is a problem with Tkinter and
# displaying some widgetes (like buttons). Text is not visible on button (Label)
# Fix: import ttk and all Buttons are ttk.Button, ttk.Checkbutton ,....
#
# style is an easy approach to set all Button with same style
#
# ttk.Radiobuttons: they are declared inside sub python modules :-( (like contourArc.py)
#

ttkStyle = ttk.Style()
ttkStyle.map(
    "C.TButton",
    foreground=[('pressed', 'blue'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')])
ttkStyle.map(
    "C.Tttk.Radiobutton",
    foreground=[('pressed', 'green'), ('active', 'red')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')])


class GeometricalFrame(Frame):
    def __init__(self, app, master, frame, title, winGeometry="900x750"):
        Frame.__init__(self)
        self.app = app
        self.parentFrame = frame
        self.title = title
        self.master = master
        self.master.geometry(winGeometry)
        self.app.master.title(title)
        self.dicMaterials = {}
        self.dicSelectedMaterial = {}
        self.dicSystemConfig = {}
        self.frmButtonsIndividualContent = Frame(
            self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)
        # format [notuse/use (0/1), GCODE, ....]
        self._standardGCodeSeq = {
            "HOMEING": [
                "G00 Z{0:08.3f} F{1:05.1f} {2}",
                "G00 X{0:08.3f} Y{1:08.3f} F{2:05.1f} {3}"
            ],
            "SPINDLE_CW": ["M3 S{0:08.4f} {1}"],
            "SPINDLE_CCW": ["M4 S{0:08.4f} {1}"],
            "TOOL": ["T{0:03d} {1}M6 {1}"],
            "PREAMBLE": ["G90 G64 G17 G40 G49 {0}"],
            "POSTAMBLE": ["G00 Z10 F100 M2 {0}"],
            "ZAXIS": [3.0, 10.0],
            "TRAVEL_SPEEDXYZ": ["500", "500", "400"],  #[X,Y,Z]
        }
        self.__loadSystemConfig()
        self.__loadMillingParameterFile()
        self.updateDefaultFields()

    def destroy(self):
        self.frmImage.destroy()
        self.frmStandardContent.destroy()
        self.frmButtonsIndividualContent.destroy()
        self.frmButtons.destroy()
        pass

    def show(self,
             showImage=True,
             showStandardContent=True,
             showStandartButton=True):
        print "Show"
        #
        if showImage:
            self.__frmImage()
        #
        if showStandardContent:
            self.__frmStandardContent()
        #
        self._frmIndividualContent()
        #
        if showStandartButton:
            self.__buttonBox()
            self.setBtnStates(state=NORMAL)
        pass

    def __frmImage(self):
        print "__frmImage"
        self.frmImage = Frame(
            self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)
        self.frmImage.grid(row=0, column=0, rowspan=5)
        self.frmImage.pack(expand=True)
        pass

    def __loadSystemConfig(self):
        print("load system json config file")
        with open("config.json", "r") as read_file:
            self.dicSystemConfig = json.load(read_file)

    def updateDefaultFields(self):
        if bool(self.dicSystemConfig):
            self._standardGCodeSeq["PREAMBLE"][0] = self.dicSystemConfig[
                "Preamble"]
            self._standardGCodeSeq["POSTAMBLE"][0] = self.dicSystemConfig[
                "Postamble"]
            self._standardGCodeSeq["ZAXIS"][0] = self.dicSystemConfig["StartZ"]
            self._standardGCodeSeq["ZAXIS"][1] = self.dicSystemConfig[
                "SafetyZ"]
            self._standardGCodeSeq["TRAVEL_SPEEDXYZ"] = self.dicSystemConfig[
                "TravelSpeedXYZ"]
        else:
            print("no system config file available")
        pass

    def __loadMillingParameterFile(self):
        '''
        load json file and save content into self.__millingparameters

        '''
        print("load JSON Milling parameter file....")
        with open("millingparameters.json", "r") as read_file:
            self.dicMaterials = json.load(read_file)

    def setMaterialDict(self, value):
        self.dicSelectedMaterial = self.getMaterialData(value)

    def upateMaterialFields(self, value):
        self.setMaterialDict(value)
        print(self.dicSelectedMaterial)
        if "ToolID" in self.dicSelectedMaterial:
            self.currentToolID.set(self.dicSelectedMaterial["ToolID"])
            self.currentSpindleRPM.set(self.dicSelectedMaterial["Spindel-RPM"])
            self.tooldia.set(self.dicSelectedMaterial["Tool dia"])
            self.speed_XY_G02G03.set(
                self.dicSelectedMaterial["Feed rate mm/min"])
            self.speed_Z_G01.set(
                self.dicSelectedMaterial["Infeed rate mm/min"])

    def getOptionMenuMillingData(self):
        '''
        create a sorted array of all defined materials
        Name of material: (Category) material => Plastic,Polystorol; Wood,beech plywood; ...
        '''
        data = []
        for (k, v) in self.dicMaterials.items():
            for list in self.dicMaterials[k]:
                s = "{0},{1}, Tool({2}mm)".format(k, list["Material"],
                                                  list["Tool dia"])
                data.append(s)
        return sorted(data)

    def getMaterialData(self, optionmenustring):
        sp = optionmenustring.split(',')
        #print (sp)
        return self.getMaterialDataDict(sp[0], sp[1])

    def getMaterialDataDict(self, category, material):
        '''
        Return a dictionary for this category and material.
        Is used to prefill entry widges like speed, tool dia, ...

        Example:
        "Material" : "PMMA 4 mm (Plexiglas)",
        "Tool" : "Single cutter",
        "ToolID" : 12,
        "Tool dia" : 2.0,
        "Feed rate 1" : 25,
        "Feed rate 2" : 1500,
        "Infeed rate" : 0.4,
        "Spindel-RPM" : 20000,
        "Info" : "Einschneid Fraeser"

        '''
        for cat in self.dicMaterials[category]:
            if cat["Material"] == material:
                return cat
        return {}

    def __frmStandardContent(self,
                             showPreamble=True,
                             showPostamble=True,
                             showSpindleAndTool=True):
        print "__frmStandardContent"
        self.frmStandardContent = Frame(
            self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)
        row = 0
        if showPreamble:
            self._preamble = StringVar()
            txt = self._standardGCodeSeq["PREAMBLE"][0].format(CR)
            self._preamble.set(txt)
            Label(
                self.frmStandardContent, text="PreGCode").grid(
                    row=row, column=0, sticky=W)
            FloatEntry(
                self.frmStandardContent,
                width=70,
                mandatory=False,
                textvariable=self._preamble).grid(
                    row=row, column=1, columnspan=6, sticky=W)

        if showPostamble:
            row += 1
            self._postamble = StringVar()
            txt = self._standardGCodeSeq["POSTAMBLE"][0].format(CR)
            self._postamble.set(txt)
            Label(
                self.frmStandardContent, text="PostGCode").grid(
                    row=row, column=0, sticky=W)
            FloatEntry(
                self.frmStandardContent,
                width=70,
                mandatory=False,
                textvariable=self._postamble).grid(
                    row=row, column=1, columnspan=6, sticky=W)

        # bugfix / requirement #10
        if showSpindleAndTool:
            row += 1
            # New in V0.12.5 -------------------------------
            choices = self.getOptionMenuMillingData()
            self.selectedMaterial = StringVar()
            self.selectedMaterial.set(choices[0])
            matWidth = len(max(choices, key=len))
            Label(
                self.frmStandardContent, text='Material').grid(
                    row=row, column=0, sticky=W)
            self.material = ttk.OptionMenu(
                self.frmStandardContent,
                self.selectedMaterial,
                *choices,
                command=self.upateMaterialFields)
            self.material.config(width=matWidth)
            self.material.grid(row=row, column=1, columnspan=2, sticky=W)

            #-----------------------------------------------
            self.currentSpindleRPM = StringVar(value="")
            self.currentToolID = StringVar(value="")
            self._spindleCCW = StringVar(value="CW")
            Label(
                self.frmStandardContent, text="ToolID").grid(
                    row=row, column=3, sticky=W)
            IntEntry(
                self.frmStandardContent,
                width=10,
                mandatory=False,
                textvariable=self.currentToolID).grid(
                    row=row, column=4, sticky=W)
            Label(
                self.frmStandardContent, text="Spindle Speed").grid(
                    row=row, column=5, sticky=W)
            IntEntry(
                self.frmStandardContent,
                width=10,
                mandatory=False,
                textvariable=self.currentSpindleRPM).grid(
                    row=row, column=6, sticky=W)
            # workaround MacOS, Mohjave with TKinter-Buttons
            #ttk.Checkbutton(self.frmStandardContent, text="Spindle CCW",
            #    var=self._spindleCCW, onvalue="CCW", offvalue="CW").grid(
            #        row=row, column=6, sticky=W
            #    )

        self.frmStandardContent.pack(expand=True, fill=BOTH)
        pass

    def _frmIndividualContent(self):
        #override in subcluss
        pass

    def __buttonBox(self):
        print "__buttonBox"
        self.frmButtons = Frame(
            self.parentFrame,
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1)

        # bugfix 25.02.2019, change from "To AXIS" to "To Console"
        self.btnAxis = ttk.Button(
            self.frmButtons,
            text="To Console",
            width=10,
            command=self.copyConsole,
            state=DISABLED,
            style="C.TButton")
        self.btnAxis.grid(row=0, column=0)

        self.btnClip = ttk.Button(
            self.frmButtons,
            text="To Clipboard",
            width=10,
            command=self.copyClipboard,
            state=DISABLED,
            style="C.TButton")
        self.btnClip.grid(row=0, column=1)

        self.btnSave = ttk.Button(
            self.frmButtons,
            text="To File",
            width=10,
            command=self.saveFile,
            state=DISABLED,
            style="C.TButton")
        self.btnSave.grid(row=0, column=2)

        self.btnGCode = ttk.Button(
            self.frmButtons,
            text="gen. GCode",
            width=10,
            command=self.showGCode,
            state=NORMAL,
            style="C.TButton")
        self.btnGCode.grid(row=0, column=3)

        #self.btnGCode = ttk.Button(self.frmButtons, text="Material", width=10,
        #    command=self.showMaterial, state=DISABLED, style="C.TButton")
        #self.btnGCode.grid(
        #        row=0, column=4
        #    )

        self.btnCancel = ttk.Button(
            self.frmButtons,
            text="Cancel",
            width=10,
            command=self.cancel,
            state=NORMAL,
            style="C.TButton")
        self.btnCancel.grid(row=0, column=4)

        self.frmButtons.pack(expand=True, fill=BOTH)

    def generateGCode(self):
        # override from subclass
        pass

    def getGCode_Homeing(self, x=0, y=0, z=10, fxy=100, fz=100):
        gc = "(HOMEING)" + CR
        gc += self._standardGCodeSeq["HOMEING"][0].format(z, fz, CR)
        gc += self._standardGCodeSeq["HOMEING"][1].format(x, y, fxy, CR)
        return gc

    def getGCode_SpindleAndTool(self, additional=""):
        temp = "(Tool handling)" + CR
        #------- Tool handling -----------
        if self.currentToolID.get() != "":
            t = int(self.currentToolID.get())
            if t < 0:
                t = 0

            msg = "{0} {1:5.2f}mm".format(self.dicSelectedMaterial["Tool"],
                                          self.dicSelectedMaterial["Tool dia"])
            temp += "(MSG, change tool to {0} {1}".format(msg, CR)
            temp += "T{0:03d} M6 {1}".format(t, CR)
        temp += "(Spindel control)" + CR
        #------- Spindle control ---------
        if self.currentSpindleRPM.get() != "":
            s = int(self.currentSpindleRPM.get())
            sdir = self._spindleCCW.get()
            if s < 0:
                s = 0
            if sdir == "CW":
                temp += "M3 S{0:04d} {1}".format(s, CR)
            else:
                temp += "M4 S{0:04d} {1}".format(s, CR)
            if s == 0:
                temp += "M5" + CR
        if additional != "":
            temp += "(additional)" + CR
            temp += additional + CR
        return temp + CR

    def getGCode_Preamble(self, additional=""):
        temp = ""
        # Preamble
        temp += CR + "(set general preamble)" + CR
        temp += self._preamble.get() + CR
        if (additional != ""):
            temp += "(additional)" + CR
            temp += additional + CR

        temp += self.getGCode_SpindleAndTool()
        return temp

    def getGCode_Postamble(self, additional=""):
        temp = ""
        # Preamble
        temp += CR + "(set general postamble)" + CR
        temp += self._postamble.get() + CR
        if (additional != ""):
            temp += "(additional)" + CR
            temp += additional + CR
        return temp

    def getGCodeCutterComp(self, compensation="G40", toolDia=0.0, x=0.0,
                           y=0.0):
        '''
        return a GCode for given cutter compensation

        This cutter compensation do not use tool table adjustment for
        tool diameters.

        if toolDia is not set (0.0) than preset tool diameter is used

        # if cutter compensation is used please remember:
        #   G41 is LEFT from path
        #   G42 is RIGHT from path
        #
        #   if our start position is at 3-clock and G41 is used, tool is inside
        #   arc (circle), because we should start LEFT from path.
        #
        #   if G42 is used, tool is outside of arc (circle) (RIGHT)
        #
        #   this behaviour depends on general contour direction (CW or CCW)
        #   CW => above behaviour
        #   CCW => G41 is RIGHT, G42 is LEFT

        '''
        gc = ""
        #if toolDia == 0.0:
        #    compensation = "G40"

        gc += "(-- cutter compensation --)" + CR
        if (compensation == "G41"):
            if toolDia == 0.0:
                gc += "G41 {1}".format(CR)
            else:
                gc += "G41.1 D{0:05.2f} X{2:08.3f} Y{3:08.3f}{1}".format(
                    toolDia, CR, x, y)
                #gc += "G41.1 D{0:05.2f}{1}".format(toolDia, CR)
        elif (compensation == "G42"):
            if toolDia == 0.0:
                gc += "G42 {1}".format(CR)
            else:
                gc += "G42.1 D{0:05.2f} X{2:08.3f} Y{3:08.3f}{1}".format(
                    toolDia, CR, x, y)
                #gc += "G42.1 D{0:05.2f}{1}".format(toolDia, CR)
        else:  # G40
            gc += "G40 {0}".format(CR)
        return gc

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
            initialdir="./",
            title="Save file",
            defaultextension="*.ngc",
            filetypes=(("Axis ", "*.ngc"), ("Gcode ", "*.gcode"), ("all files",
                                                                   "*.*")))
        if (fname == None):
            # cancle button
            return None
        print("Save gcode to '{}'".format(fname))
        f = open(fname, "w")
        f.write(gc)
        f.close()
        pass

    def copyConsole(self, event=None):
        print("---------------- copyConsole -----------------")
        gc = self.getGCode()
        if gc is None:
            return None
        sys.stdout.write(self.getGCode())
        #self.quit()

    def showGCode(self, event=None):
        gc = self.getGCode()
        if gc is None:
            return None
        d = GCodeDialog(self.app, title="generated GCode")
        d.init(gc)
        d.update(gc)
        pass

    def showMaterial(self, event=None):
        data = {}
        d = EntryGridDialog(self.app, title="MaterialParameters")
        d.init(data)
        d.update(data)
        pass

    def setBtnStates(self, state):
        self.btnClip.config(state=state)
        self.btnSave.config(state=state)
        self.btnAxis.config(state=state, default=ACTIVE)
        self.btnGCode.config(state=state)

    def defaultUserValidation(self):
        pre = self._preamble.get()
        post = self._postamble.get()
        try:
            spindle = int(self.currentSpindleRPM.get())
        except ValueError:
            spindle = -1
        try:
            toolID = int(self.currentToolID.get())
        except ValueError:
            toolID = -1

        if pre == "":
            self.MessageBox(
                state="WARN",
                title="Warn",
                text="Are you shure? There is no preamble gcode available")
            return False

        if post == "":
            self.MessageBox(
                state="WARN",
                title="Warn",
                text="Are you shure? There is no postamble gcode available")
            return False

        if (spindle < -1 or toolID < -1):
            self.MessageBox(
                state="INFO",
                title="INFO",
                text="You set no tool id and/or spindel control")
            return True
        return True

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
        if self.defaultUserValidation() == False:
            return None
        if self.userInputValidation() == False:
            return None
        gc = "%"
        #
        # removed because some trouble with GCode-Interpreters (BK-13.12.2018)
        gc += '''
; (--------------------------)
; (          __              )
; (  _(\    |@@|             )
; ( (__/\__ \--/ __          )
; (    \___|----|  |   __    )
; (        \ }{ /\ )_ / _\   )
; (        /\__/\ \__O (__   )
; (       (--/\--)    \__/   )
; (       _)(  )(_           )
; (      `---''---`          )
; (    (c) by LunaX 2018     )
; (--------------------------)
         '''
        gc += CR
        gc += self.generateGCode()
        gc += "%" + CR
        return gc

    #------ EXIT --------------------------
    def cancel(self, event=None):
        print "cancel"
        #self.destroy()
        self.master.quit()
        pass

    def MessageBox(self, state="INFO", title="", text=""):
        if state == "INFO":
            tkMessageBox.showinfo(title, text)
        elif state == "WARN":
            tkMessageBox.showinfo(title, text)
        elif state == "ERROR":
            tkMessageBox.showerror(title, text)
        else:
            tkMessageBox.showtitle("!!!unknown - State !!!", text)

    def getDepthSteps(self, total, step):
        '''
        calculate how many depth steps we need to mill to total depth.
        Return two values:
            1. Value = numberOfWindings
            2. Value = rest depth
        '''
        r = round((total % step), 3)
        w = int(abs(total / step))
        return w, r


class ToolTip:
    '''
    It creates a tooltip for a given widget as the mouse goes on it.

    see:

    http://stackoverflow.com/questions/3221956/
           what-is-the-simplest-way-to-make-tooltips-
           in-tkinter/36221216#36221216

    http://www.daniweb.com/programming/software-development/
           code/484591/a-tooltip-class-for-tkinter

    - Originally written by vegaseat on 2014.09.09.

    - Modified to include a delay time by Victor Zaccardo on 2016.03.25.

    - Modified
        - to correct extreme right and extreme bottom behavior,
        - to stay inside the screen whenever the tooltip might go out on
          the top but still the screen is higher than the tooltip,
        - to use the more flexible mouse positioning,
        - to add customizable background color, padding, waittime and
          wraplength on creation
      by Alberto Vassena on 2016.11.05.

      Tested on Ubuntu 16.04/16.10, running Python 3.5.2

    TODO: themes styles support
    '''

    def __init__(self,
                 widget,
                 bg='#FFFFEA',
                 pad=(5, 3, 5, 3),
                 text='widget info',
                 waittime=400,
                 wraplength=300):

        self.waittime = waittime  # in miliseconds, originally 500
        self.wraplength = wraplength  # in pixels, originally 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<FocusIn>", self.onEnter)
        self.widget.bind("<FocusOut>", self.onLeave)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.bg = bg
        self.pad = pad
        self.id = None
        self.tw = None

    def onEnter(self, event=None):
        self.schedule()

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show(self):
        def tip_pos_calculator(widget,
                               label,
                               tip_delta=(10, 5),
                               pad=(5, 3, 5, 3)):

            w = widget

            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()

            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])

            mouse_x, mouse_y = w.winfo_pointerxy()

            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height

            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0

            offscreen = (x_delta, y_delta) != (0, 0)

            if offscreen:

                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width

                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height

            offscreen_again = y1 < 0  # out on the top

            if offscreen_again:
                # No further checks will be done.

                # TIP:
                # A further mod might automagically augment the
                # wraplength when the tooltip is too high to be
                # kept inside the screen.
                y1 = 0

            return x1, y1

        bg = self.bg
        pad = self.pad
        widget = self.widget

        # creates a toplevel window
        self.tw = Toplevel(widget)

        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)

        win = Frame(self.tw, background=bg, borderwidth=0)
        label = Label(
            win,
            text=self.text,
            justify=LEFT,
            background=bg,
            relief=SOLID,
            borderwidth=0,
            wraplength=self.wraplength)

        label.grid(padx=(pad[0], pad[2]), pady=(pad[1], pad[3]), sticky=NSEW)
        win.grid()

        x, y = tip_pos_calculator(widget, label)

        self.tw.wm_geometry("+%d+%d" % (x, y))

    def hide(self):
        tw = self.tw
        if tw:
            tw.destroy()
        self.tw = None
