from Tkinter import *
from tkFont import Font
from math import *
import tkMessageBox
import os
import math


class Dialog(Toplevel):
#
    def __init__(self, parent, title = "??", xSize = 350, ySize = 250):

        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.sourceFont = Font(family="Courier", size=12)
        if title:
            self.title(title)

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+xSize,
                                  parent.winfo_rooty()+ySize))



    def init(self, data):
        self.result = None
        self.data = ""

        self.frmbody = Frame(self)
        self.update(data)
        self.initial_focus = self.body(self.frmbody)
        self.frmbody.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if self.initial_focus == None:
            self.initial_focus = self
        self.initial_focus.focus_set()
        self.wait_window(self)
        pass
    #
    # construction hooks
    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        btnOK = Button(box, text="OK", width=10,
            command=self.ok, default=ACTIVE)
        btnOK.pack(side=LEFT, padx=5, pady=5)

        btnCancel = Button(box, text="Cancel", width=10,
            command=self.cancel)
        btnCancel.pack(side=LEFT, padx=5, pady=5)


        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        #print "in OK"
#        self.withdraw()
#        self.update_idletasks()
#        self.apply()
        self.cancel()


    def cancel(self, event=None):
        #print "in CANCEL"
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override

    def update(self, data):
        pass


#----------------------------------------------------------------------------
# new individual dialogs
#----------------------------------------------------------------------------
class GCodeDialog(Dialog):

    def update(self, data):
        print "setData len({})".format(len(self.data))
        self.data = data
        pass


    def apply(self):
        pass

    def body(self, master):
        # self.frmbody is a frame from superclass
        self.frmbody.grid(row=0, column=0)

        self.l01 = Label(self.frmbody, text="GCode")
        self.l01.grid(row=0,column=0)

        self.txtGCode = Text(self.frmbody, width=60, height=40, font=self.sourceFont)
        self.txtGCode.config(
            highlightbackground="darkgray",
            highlightcolor="darkgray",
            highlightthickness=1
        )
        self.txtGCode.grid(
            row=1, column=0, rowspan=5)
        self.txtGCode.insert(END, self.data)
        self.txtGCode.bind("<Control-KeyRelease-a>", self.__cbSelectAll)
        pass

    def __cbSelectAll(self, event):
        print ("__cbSelectAll(self, event ({})".format(event))
        event.widget.tag_add(SEL, "1.0", END)
        event.widget.mark_set(INSERT, "1.0")
        event.widget.see(INSERT)
        return 'break'

#----------------------------------------------------------------------------
# new Entry widgets
#----------------------------------------------------------------------------
class ValidatingEntry(Entry):
    def __init__(self, master, validate="", vcmd=None, signed = "s", mandatory=False, **kw):
        apply(Entry.__init__,(self, master), kw)
        self.__mandatory = mandatory
        if signed != "s":   # signed
            signed = "u"    # unsigned
        self.__signed = signed
        self.tempVCMD = vcmd
        vcmd = (self.register(self.__isValid), '%P')
        self.config(validate='focusout', vcmd=vcmd)
        vcmd = (self.register(self.__isInvalid), '%W')
        self.config(invalidcommand=vcmd)
        self.isValueAvailable = True,
        #self.insert(0,value)


    def __isValid(self, value):
        # value contains %P
        self.isValueAvailable = True
        if self.__mandatory:
            print "__mandatory {}".format(value)
            if value == None or not value or len(value) == 0:
                # empty mandatory field
                self.config({"background": "Red"})
                self.isValueAvailable = False
                return True
        else:
            if not value:
                # empty fields are allowed
                #print "is mandatory "
                return True
        # value is set, check if valid
        value = self.validate(value)
        if math.isnan(float(value)):
                # not a valid value
                return False
        if (self.__signed == "u" and float(value) < 0.0):
            # unsigned values are not negativ
            return False

        # valid value
        self.config({"background": "White"})

        #
        #
        if (self.tempVCMD != None):
            self.tempVCMD(value)
        return True

    def __isInvalid(self, widgetName):
        # called automatically when the
        # validation command returns 'False'
        #print "__isInvalid {}:{}".format(widgetName, self.get())
        # get entry widget
        self.delete(0,END)

        # return focus to integer entry
        self.focus_set()
        self.bell()

        # set background color to red
        if self.__mandatory:
            if self.get() == None or len(self.get()) == 0:
                self.config({"background": "Red"})
        return False

    def validate(self, value):
        # override
        return value


class IntegerEntry(ValidatingEntry):

    def validate(self, value):
        try:
            if value:
                v = int(value)
            return v
        except ValueError:
            return float('nan')

class FloatEntry(ValidatingEntry):

    def validate(self, value):
        #print "call me from super class"
        try:
            if value:
                v = float(value)
            return v
        except ValueError:
            #print "FloatError"
            return float('nan')

class FloatEntry2(ValidatingEntry):
    def __init__(self, master, vcmd=None, validate=None, min=None, max=None, mandatory=False, **kw):
        ValidatingEntry.__init__(master, mandatory, vcmd, validate,**kw)
        self.__min = min
        self.__max = max


    def validate(self, value):
        #print "call me from super class"
        try:
            if value:
                v = float(value)

            return v
        except ValueError:
            #print "FloatError"
            return float('nan')
