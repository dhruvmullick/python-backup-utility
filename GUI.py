import sys
from Tkinter import *
import Tkconstants, tkFileDialog
import datetime
import ttk
import main

dirtext = 'Select your pictures folder'
filetext = 'Select your exception file'
dirtext1 = 'Select destination of image'

# file and directory function
root = Tk()
Ldir = []
Ldirignore = []
dirn = []
ldir1 = []
dirname2=""

def askdirectory():
    global Ldir
    dirname = tkFileDialog.askdirectory(parent=root, title=dirtext)
    # btn["text"] =str(btn["text"]+str(dirname)) if dirname else dirtext
    print dirname
    T.insert(INSERT, dirname+"\n")
    Ldir += [(dirname)]


def openfile():
    global Ldir
    filename = tkFileDialog.askopenfilename(parent=root, title=filetext)  # filename not filehandle
    #  filebut["text"]= str(filename) if filename else filetext
    print filename
    T.insert(INSERT, filename+"\n")
    Ldir +=[(filename)]


def askdirectory1():
    global ldir1
    dirname1 = tkFileDialog.askdirectory(parent=root, title=dirtext)
    print dirname1
    T4.insert(INSERT, dirname1+"\n")
    ldir1 += [(dirname1)]


def openfile1():
    global ldir1
    filename1 = tkFileDialog.askopenfilename(parent=root, title=filetext)
    print filename1
    T4.insert(INSERT, filename1+"\n")
    ldir1 += [(filename1)]


def askd1():
    global dirn
    dirname = tkFileDialog.askdirectory(parent=root, title=dirtext1)
    T2.insert(INSERT, dirname+"\n")
    dirn += [(dirname)]
    # Dest["text"] =str(dirn) if dirn else dirtext

def  DestSelect():
    global dirname2
    dirname2 = tkFileDialog.askdirectory(parent=root, title=dirtext1)

def Callfun():
    global Ldir,dirname2,ldir1
    main.Backupnow(Ldir,dirname2,[])

root.title('Backup Implementation')
#   *** NOTEBOOK***
n = ttk.Notebook(root)
# fstatusr=Frame(root)
# fstatusr.grid(sticky=S+W)

# fstatusl=Frame(root)
# fstatusl.grid(sticky=S+E)
f1 = Frame(n, bd=1, relief=SUNKEN)  # first page, which would get widgets gridded into it
f2 = Frame(n)  # second page
f3 = Frame(n)
f4 = Frame(n)

n.add(f1, text='Backup files')
n.add(f2, text='Ignore List')
n.add(f3, text='History')
n.add(f4, text='ISO image')
n.pack(fill=BOTH)

T = Text(f1)
T.pack()
b1 = Button(f1, text="Browse directories", command=askdirectory)
b1.pack()
b2 = Button(f1, text="Browse files", command=openfile)
b2.pack()
T2 = Text(f4, height=10)
T2.pack()
T2.insert(INSERT, "Choose the destination where you want your ISO image to be ceated \n")
b10 = Button(f4, text="get ISO image", command=askd1)
b10.pack()
Destdir = Button(f1, text="Select Backup Destination", command=DestSelect)
Destdir.pack()
BackupNow = Button(f1, text="Backup Now", command=Callfun)
b2.pack()


#  *** STATUS BAR ***
now = datetime.datetime.now()
status1 = Label(root, text= "Preparing to Backup...",bd=1,relief=SUNKEN, anchor=W)
status1.pack(side=BOTTOM, fill=X)
#  enter the present time and date at the right

str = '%s : %s' %(now.hour, now.minute)

status2 = Label(root, text=str, bd=1,relief=SUNKEN, anchor=E)  # create a function so that the status bar#  changes text evry time a button is clicked
status2.pack(side=BOTTOM, fill=X)  # enter the present time and date at the right
T4 = Text(f2, height=20)
T4.pack()
b11 = Button(f2, text="Browse directories to ignore", command=askdirectory1)
b11.pack()
b21 = Button(f2, text="Browse files to ignore", command=openfile1)
b21.pack()
lst1 = ['.pdf', '.txt', '.rtf', '.ppt']
var1 = StringVar()
var1.set('select from the options below')
drop = OptionMenu(f2, var1, *lst1)
drop.grid(row=15)
drop.pack()

root.mainloop()
#  check whether the last char
#  check file and directory and extensions.. Backup now button
#  destination field
#  drop down custom input