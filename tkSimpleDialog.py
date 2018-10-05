from Tkinter import *
from tkFont import Font
from math import *
import tkMessageBox
import os
import math


class Dialog(Toplevel):

    def __init__(self, parent, title = None):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.frmbody = Frame(self)
        self.initial_focus = self.body(self.frmbody)
        self.frmbody.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+350,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)
        self.numberOfMandatoryFields = 0


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

        btnOK = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        btnOK.pack(side=LEFT, padx=5, pady=5)
        btnCancel = Button(box, text="Cancel", width=10, command=self.cancel)
        btnCancel.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        #btnOK.config(state=DISABLED)
        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        #print "in OK"
        self.withdraw()
        self.update_idletasks()

        self.apply()

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

class ValidatingEntry(Entry):
    def __init__(self, master, signed = "s", value="", mandatory=False, **kw):
        apply(Entry.__init__,(self, master), kw)
        self.__mandatory = mandatory
        if signed != "s":   # signed
            signed = "u"    # unsigned
        self.__signed = signed
        vcmd = (self.register(self.__isValid), '%P')
        self.config(validate='focusout', vcmd=vcmd)
        vcmd = (self.register(self.__isInvalid), '%W')
        self.config(invalidcommand=vcmd)
        self.isValueAvailable = True,
        self.insert(0,value)

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
