#!/usr/bin/python
from Tkinter import *
dirtext='Select your pictures folder'
filetext= 'Select your exception file'
import Tkconstants, tkFileDialog

import ttk
def askdirectory():

    dirname = tkFileDialog.askdirectory(parent=root, title=dirtext)
    b1["text"] = str(dirname) if dirname else dirtext

def openFile():
    filename = tkFileDialog.askopenfilename(parent=root,title=filetext) ## filename not filehandle
    filebut["text"]= str(filename) if filename else filetext

root = Tk()
root.title('Backup Implementation')
#the notebook with three pages
n = ttk.Notebook(root)
f1 = Frame(n)  # first page, which would get widgets gridded into it

f2 = Frame(n)  # second page

f3 = Frame(n)
n.add(f1, text='Backup files')
n.add(f2, text='Exception files')
n.add(f3, text='History')
n.pack(fill=BOTH)
label_1 = Label(f1, text="Backup Files")
label_1.grid(row=0)
entry_1 = Entry(f1)
entry_1.grid(row=0,column=2,sticky=W+S+E+N)
b1=Button(f1,text='Browse',command=askdirectory)
b1.grid(row=1,column=0)
filebut=Button(f2,text='Browse exception files',command=openFile)
filebut.grid(row=1,column=0)
#browse button
#labels to specify what to do

root.mainloop()