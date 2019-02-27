from Tkinter import *
from tkFont import Font
from math import *
import tkMessageBox
import os
import math
import json
import ttk

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
        print("Dialog::init")
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
        print("Dialog::buttonbox")
        box = Frame(self)

        # Bugfix: 25.02.2019, change to ttk.Button and insert style
        btnOK = ttk.Button(box, text="OK", width=10,
            command=self.ok, default=ACTIVE, style="C.TButton")
        btnOK.pack(side=LEFT, padx=5, pady=5)

        # Bugfix: 25.02.2019, change to ttk.Button and insert style
        btnCancel = ttk.Button(box, text="Cancel", width=10,
            command=self.cancel, style="C.TButton")
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
        self.txtGCode.bind("<Command-KeyRelease-a>", self.__cbSelectAll)
        self.txtGCode.bind("<Command-a>", self.__cbSelectAll)
        pass

    def __cbSelectAll(self, event):
        print ("__cbSelectAll(self, event ({})".format(event))
        event.widget.tag_add(SEL, "1.0", END)
        event.widget.mark_set(INSERT, "1.0")
        event.widget.see(INSERT)
        return 'break'


class EntryGridDialog(Dialog):
    '''
    open a Dialog with a Grid inside
    '''

    def __init__(self, parent, title = "??", xSize = 700, ySize = 250):
        Dialog.__init__(self, parent, title, xSize, ySize)
        self.json_fn    = "./millingparameters.json"
        self.head_fmt    = [
                        "{:20}", "{:8}", "{:15}", "{:8}", "{:12}", "{:12}",
                        "{:15}", "{:15}", "{:25}"]
        self.cell_fmt    = [
                        "{:15}", "{:4d}", "{:15}", "{:05.3f}", "{:04.1f}", "{:05.1f}",
                        "{:04.1f}", "{:5d}", "{:25}"]
        self.colH1      = [
                        "Material", "ToolID", "Tool", "Tool dia", "Feed rate 1",
                        "Feed rate 2", "Infeed rate", "Spindel-RPM", "Info"]
        self.colH2      = [
                        "(String)", "(int)", "(String)", "(mm)", "(mm/sec)",
                        "(mm/min)", "(mm/min)", "(rpm)", "(String)"]
        self.__imageNames = []
        self.__json = []
        self.loadJSON()
        self.materialList = self.getAllMaterials()
        self.rowList = self.getMaterialParameterList("Metal")
        self.frmtable = Frame(self)

    def init(self, data):
        print("EntryGridDialog::init")
        Dialog.init(self, data)
        #
        # setup the grid with headers and cells
        pass

    def buttonbox(self):
        print("EntryGridDialog::buttonbox")
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)

        btnOK = ttk.Button(box, text="Save", width=10,
            command=self.ok, style="C.TButton")
        btnOK.pack(side=LEFT, padx=5, pady=5)

        btnLoad = ttk.Button(box, text="Load", width=10,
            command=self.load, style="C.TButton")
        btnLoad.pack(side=LEFT, padx=5, pady=5)

        btnCancel = ttk.Button(box, text="Cancel", width=10,
            command=self.cancel, default=ACTIVE, style="C.TButton")
        btnCancel.pack(side=LEFT, padx=5, pady=5)


        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()
        pass

    def load(self, event=None):
        pass

    def update(self, data):
        self.data = data
        pass

    def apply(self):
        pass

    def body(self, master):
        row = 0
        self.frmbody.grid(row=row, column=0)

        choices = self.getAllMaterials()
        self.__materials = StringVar()
        self.__materials.set(choices[0])
        currentMat = self.__materials.get()

        Label(self.frmbody, text='Materials').grid(row=row, column=0, columnspan=10, sticky=W)
        OptionMenu(self.frmbody,
            self.__materials, *choices, command=self._changeImage).grid(
            row=row, column=1)
        #
        # TableGrid
        row += 1
        self.table = EntryGrid(self.frmtable, self.colH1, self.rowList, self.head_fmt, self.cell_fmt)
        #self.table.grid(row=row,column=0)
        #self.table.make_header(row)
        self.gridDict = {}

        for r in range(0,len(self.rowList)):
            ''' read every cell in this row and populate values into widget '''
            cells = self.getMaterialParameterRow(currentMat,r)
            for x, key in enumerate(self.colH1):
                value = cells[key]
                w = EntryWidget(self.frmtable, x, r+1)
                self.gridDict[(x,r)] = value
                def handler(event, col=x, row=r):
                    return self.__entryhandler(col, row)
                w.bind(sequence="<FocusOut>", func=handler)



#        print ("Header: {}".format(self.colH1))
#        for i in range(1, len(self.colH1)):
#            print ("Row: {}".format(self.rowList))
#            for j in range(len(self.rowList)):
#                w = EntryWidget(self.frmtable, i-1, j+1)
#                w.grid(row = row, stick=W)
#                self.gridDict[(i-1,j)] = w.value
#                def handler(event, col=i-1, row=j+row):
#                    return self.table.entryhandler(col, row)
#                w.bind(sequence="<FocusOut>", func=handler)
        self.frmtable.pack()
        pass

    def _changeImage(self, event=None):
        print ("EntryGridDialog::changeImage")
        pass

    #------------------------------------------------------------
    # JSON handling stuff
    #------------------------------------------------------------
    def loadJSON (self):
        print ("load {}".format(self.json_fn))
        with open(self.json_fn, 'r') as f:
            self.__json = json.load(f)

        pass

    def saveJSON(self):
        print ("save {}".format(self.json_fn))
        with open(self.json_fn, 'w') as f:
                json.dump(self.__json, f)
        pass

    def getAllMaterials(self):
        '''
            return a list of all configured materials inside JSON file
            This method is used to fill list box with materials
        '''
        materials = []
        for material in self.__json:
            print ("Material {}".format(material))
            materials.append(material)

        return materials

    def getMaterialParameterList(self, material):
        '''
            return a list of all entries for this material
        '''
        parameters = self.__json[material]
        print parameters
        return parameters

    def getMaterialParameterRow(self, material, idx):
        '''
            return a special paramter for this material
            return an empty list, if idx is out side range
        '''
        parameters = self.getMaterialParameterList(material)
        if idx >= len(parameters):
            return {}
        row = parameters[idx]
        return row

    #------------------------------------------------------------
    # EntryGrid stuff
    #------------------------------------------------------------




#----------------------------------------------------------------------------
# Special Entry widgets
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

class IntEntry(ValidatingEntry):

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

class StringEntry(ValidatingEntry):

    def validate(self, value):
        if value == "" and self.mandatory == True:
            raise ValueError("field is empty")
        pass


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


#----------------------------------------------------------------------------
#
# a TK-Grid build with ENTRY-Widgets and a header row
#
#----------------------------------------------------------------------------
#import Tkinter
from time import sleep

textFont1 = ("Arial", 10, "bold italic")
textFont2 = ("Arial", 16, "bold")
textFont3 = ("Arial", 8, "bold")
textFont4 = ("Helvetica", 10, "bold")
textFont5 = ("Helvetica", 8, "bold")

class LabelWidget(Entry):
    def __init__(self, master, x, y, text, width=12):
        self.text = StringVar()
        self.text.set(text)
        Entry.__init__(self, master=master)
        self.config(relief="ridge", font=textFont1,
                    bg="#ffffff000", fg="#000000fff",
                    readonlybackground="#ffffff000",
                    justify='center',width=width,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=x, row=y)

class EntryWidget(Entry):
    def __init__(self, master, x, y, state="normal", width=12):
        Entry.__init__(self, master=master)
        self.value = StringVar()
        self.config(textvariable=self.value, width=width,
                    relief="ridge", font=textFont1,
                    bg="#ddddddddd", fg="#000000000",
                    justify='center', state=state)
        self.grid(column=x, row=y)
        self.value.set("")

class EntryGrid(Entry):
    '''
    Special Entry which create a couple of input cells.

    A Grid contain one or two header rows and several data rows

    based on size of colList a number of columns are created
    based on size of rowList a number of rows are created
    based on colFmt input is formatted

    '''
    def __init__(self, master, colList, rowList, headFmt, cellFmt, title="Entry Grid", state="DISABLED"):
        self.cols = colList[:]
        self.colH1 = colList[:]
        self.colH2 = colList[:]
        self.colList = colList[:]
        self.colList.insert(0, "")
        self.rowList = rowList
        self.colFmt = cellFmt
        self.headFmt = headFmt
        self.title = title
        self.master = master
        self.make_header()

        self.gridDict = {}

    def make_header(self, id=1, row=0):
        ''' create header row(s)'''
        header = []
        if id==1:
            header = self.colH1
        if id==2:
            header = self.colH2

        self.hdrDict = {}
        for i, label in enumerate(header):
            # calculate cell width
            hfmt = self.headFmt[i]
            str = hfmt.format("x")
            width = len(str)
            def handler(event, col=i, row=row, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.master, i, 0, label, width)
            self.hdrDict[(i,0)] = w
            w.bind(sequence="<KeyRelease>", func=handler)

    def entryhandler(self, col, row):
#        s = self.gridDict[(col,row)].get()
#        if s.upper().strip() == "EXIT":
#            self.destroy()
#        elif s.upper().strip() == "DEMO":
#            self.demo()
#        elif s.strip():
#            print s
        pass

    def __headerhandler(self, col, row, text):
        ''' has no effect when Entry state=readonly '''
        self.hdrDict[(col,row)].text.set(text)

    def get(self, x, y):
        return self.gridDict[(x,y)].get()

    def set(self, x, y, v):
        self.gridDict[(x,y)].set(v)
        return v

    def fillRow(self, row, data):
        pass

    def getRow(self, row):
        data = {}
        return data

# class EntryGrid(Tkinter.Tk):
#     ''' Dialog box with Entry widgets arranged in columns and rows.'''
#     def __init__(self, colList, rowList, title="Entry Grid"):
#         self.cols = colList[:]
#         self.colList = colList[:]
#         self.colList.insert(0, "")
#         self.rowList = rowList
#         Tkinter.Tk.__init__(self)
#         self.title(title)
#
#         self.mainFrame = Tkinter.Frame(self)
#         self.mainFrame.config(padx='3.0m', pady='3.0m')
#         self.mainFrame.grid()
#         self.make_header()
#
#         self.gridDict = {}
#         for i in range(1, len(self.colList)):
#             for j in range(len(self.rowList)):
#                 w = EntryWidget(self.mainFrame, i, j+1)
#                 self.gridDict[(i-1,j)] = w.value
#                 def handler(event, col=i-1, row=j):
#                     return self.__entryhandler(col, row)
#                 w.bind(sequence="<FocusOut>", func=handler)
#         self.mainloop()
#
#     def make_header(self):
#         self.hdrDict = {}
#         for i, label in enumerate(self.colList):
#             def handler(event, col=i, row=0, text=label):
#                 return self.__headerhandler(col, row, text)
#             w = LabelWidget(self.mainFrame, i, 0, label)
#             self.hdrDict[(i,0)] = w
#             w.bind(sequence="<KeyRelease>", func=handler)
#
#         for i, label in enumerate(self.rowList):
#             def handler(event, col=0, row=i+1, text=label):
#                 return self.__headerhandler(col, row, text)
#             w = LabelWidget(self.mainFrame, 0, i+1, label)
#             self.hdrDict[(0,i+1)] = w
#             w.bind(sequence="<KeyRelease>", func=handler)
#
#     def __headerhandler(self, col, row, text):
#         ''' has no effect when Entry state=readonly '''
#         self.hdrDict[(col,row)].text.set(text)
#
#     def __entryhandler(self, col, row):
#         s = self.gridDict[(col,row)].get()
#         if s.upper().strip() == "EXIT":
#             self.destroy()
#         elif s.upper().strip() == "DEMO":
#             self.demo()
#         elif s.strip():
#             print s
#
#     def demo(self):
#         ''' enter a number into each Entry field '''
#         for i in range(len(self.cols)):
#             for j in range(len(self.rowList)):
#                 sleep(0.25)
#                 self.set(i,j,"")
#                 self.update_idletasks()
#                 sleep(0.1)
#                 self.set(i,j,i+1+j)
#                 self.update_idletasks()
#
#     def __headerhandler(self, col, row, text):
#         ''' has no effect when Entry state=readonly '''
#         self.hdrDict[(col,row)].text.set(text)
#
#     def get(self, x, y):
#         return self.gridDict[(x,y)].get()
#
#     def set(self, x, y, v):
#         self.gridDict[(x,y)].set(v)
#         return v

#if __name__ == "__main__":
#    cols = ['A', 'B', 'C', 'D']
#    rows = ['1', '2', '3', '4']
#    app = EntryGrid(cols, rows)
