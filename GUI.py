import sys
from Tkinter import *
import Tkconstants, tkFileDialog
import datetime
import ttk
import main
import createISO

dirtext = 'Select your pictures folder'
filetext = 'Select your exception file'
dirtext1 = 'Select destination of image'

# file and directory function
root = Tk()
Ldir = []
Ldirignore = []
dirn = []
ldir1 = {}
dirname2 = ""
ct = 0
ct1 = 0
LC=[]
LD=[]

def askdirectory():
    global Ldir
    global ct
    dirname = tkFileDialog.askdirectory(parent=root, title=dirtext)
    if dirname != "":
      ct=ct+1
      str1 = '%s '%ct
      T.insert(INSERT,str1+". " + dirname+"\n")
      Ldir += [dirname]


def openfile():
    global Ldir
    global ct
    filename = tkFileDialog.askopenfilename(parent=root, title=filetext)  # filename not filehandle
    if filename != "":
     ct=ct+1
     str1 = '%s '%ct
     T.insert(INSERT,str1+". " + filename+"\n")
     Ldir += [filename]


def askdirectory1():
    global ldir1
    global ct1
    dirname1 = tkFileDialog.askdirectory(parent=root, title=dirtext)
    if dirname1 != "":
     ct1=ct1+1
     str1 = '%s '%ct1
     T4.insert(INSERT, str1+". " + dirname1+"\n")
     ldir1[dirname1] = 1


def openfile1():
    global ldir1
    global ct1
    filename1 = tkFileDialog.askopenfilename(parent=root, title=filetext)
    if filename1 != "":
     ct1=ct1+1
     str1 = '%s '%ct1
     T4.insert(INSERT,str1+". "+ filename1+"\n")
     ldir1[filename1]=1


def askd1():
    global dirn
    dirn = tkFileDialog.askdirectory(parent=root, title=dirtext1)
    if dirn != "":
      T2.insert(INSERT, dirn+"\n")

    # Dest["text"] =str(dirn) if dirn else dirtext

def  DestSelect():
    global dirname2
    dirname2 = tkFileDialog.askdirectory(parent=root, title=dirtext1)

#create iso
def createf():
    global dirname2,dirn
    createISO.isoCreator(dirname2,dirn)

def Callfun():
    global Ldir,dirname2,ldir1,T,ct,ct1,var1
    global Ldirignore,dirn,LC,LD

    if var1.get()!=None:
        ldir1[var1.get()] = 1
    (LC,LD) = main.Backupnow(Ldir,dirname2,ldir1)
    now = datetime.datetime.now()
    str1 = '%s : %s : %s ' %(now.day, now.month, now.year)
    str = '%s : %s ' %(now.hour, now.minute)
    #print the contents of LC and LD
    # print 'Call fun'
    # print LC
    # print LD
    T5.insert(INSERT, "Backup has been created at"+dirname2+" \n at "+str+" on "+str1+"\n")
    T5.insert(INSERT, "Files last backed up are :\n")
    T5.insert(INSERT, "Copied files are :\n")
    for x in LC:
        T5.insert(INSERT, x + "\n")
    T5.insert(INSERT, "Deleted files are :\n")
    for x in LD:
        T5.insert(INSERT, x + "\n")
    T.delete("1.0",END)
    ct=0
    ct1=0

    # clear everything
    Ldir = []
    Ldirignore = []
    dirn = []
    ldir1 = {}
    ct = 0
    ct1 = 0
    LC=[]
    LD=[]


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

scrollbar = Scrollbar(f1)
scrollbar.pack(side=RIGHT, fill=Y)
T = Text(f1, wrap=WORD, yscrollcommand=scrollbar.set, font=("helvetica", 12))
T.pack()
scrollbar.config(command=T.yview)

b1 = Button(f1, text="Browse directories", command=askdirectory)
b1.pack()
b2 = Button(f1, text="Browse files", command=openfile)
b2.pack()
T2 = Text(f4, height=10)
T2.pack()
T2.insert(INSERT, "Choose the destination where you want your ISO image to be ceated \n")

b10 = Button(f4, text="get destination of ISO image", command=askd1)
b10.pack()

cre = Button(f4, text="Create ISO image", command=createf)
cre.pack()

Destdir = Button(f1, text="Select Backup Destination", command=DestSelect)
Destdir.pack()
BackupNow = Button(f1, text="Backup Now", command=Callfun)
BackupNow.pack()
b2.pack()


#  *** STATUS BAR ***
now = datetime.datetime.now()
status1 = Label(root, text= "Preparing to Backup...",bd=1,relief=SUNKEN, anchor=W)
status1.pack(side=BOTTOM, fill=X)
#  enter the present time and date at the right

str = '%s : %s' %(now.hour, now.minute)
status2 = Label(root, text=str, bd=1,relief=SUNKEN, anchor=E)  # create a function so that the status bar#  changes text evry time a button is clicked
status2.pack(side=BOTTOM, fill=X)  # enter the present time and date at the right
scrollbar1 = Scrollbar(f2)
scrollbar1.pack(side=RIGHT, fill=Y)
T4 = Text(f2, wrap=WORD, yscrollcommand=scrollbar.set, font=("helvetica", 12))
T4.pack()
scrollbar1.config(command=T.yview)
scrollbar2 = Scrollbar(f3)
scrollbar2.pack(side=RIGHT, fill=Y)
T5 = Text(f3, wrap=WORD, yscrollcommand=scrollbar.set, font=("helvetica", 12))
T5.pack()
scrollbar2.config(command=T.yview)

b11 = Button(f2, text="Browse directories to ignore", command=askdirectory1)
b11.pack()
b21 = Button(f2, text="Browse files to ignore", command=openfile1)
b21.pack()


lst1 = ['None','.pdf', '.txt', '.rtf', '.ppt']
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