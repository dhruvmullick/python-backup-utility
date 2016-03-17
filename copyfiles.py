"""
Copy functions
1. copyBasic - to implement basic copying of single file/tree
2. copyFull - to copy files and folders taking into consideration the ignored list
"""

import os
import shutil
import time

#copyBasic - Recursive copy. src can be a folder or a file, and dst path shouldn't exist is folder copied, but doesn't matter if file copied
#better than the default copy2() function, as we can specify the new filename as well, and take care of the errors.
def copyBasic(src,dst):
    if os.path.isfile(src): #src is a file.
        if not os.path.exists(dst): #if it is a file then dst folder must exist
            os.mkdir(dst)
        # L=src.rsplit('.',1) #obtain the source and dest path
        # L[0]=L[0]+'_new'      #use this to keep a new name for the copied file
        # src=L[0]+'.'+L[1]
        dst=dst+os.path.basename(src)  #copy src file with a new name to dst folder
        shutil.copyfile(src,dst)
        return
    try:
        shutil.copytree(src, dst)   #copy entire directory. dst directory shouldn't exist already
    except OSError as exc:  #if it is a file. But this doesn't change the name of the file to a new name. So we have created our own function above
         print "Exception occured"
    #     if exc.errno == errno.ENOTDIR:
    #         shutil.copy2(src, dst)
    #     else:
    #         raise
    #


#copyFull - copy files from folder src to dst recursively. If the file is an exception, then ignore it.
def copyFull(src, dst, ignoreList):

    if(ignoreList.has_key(src)):
        print '\n-----\nCopied\n-----\n'

    for root,dirs,files in os.walk(src):   #walk through the directory

        dirs[:] = [d for d in dirs if os.path.join(root,d) not in ignoreList] #modify dirs so that you enter only if the subdirectory is not in ignoreList
        os.chdir(root)

        for hereFile in files:
            if(hereFile[0]=='.'):   #don't copy hidden files
                continue

            print 'file name = ' + hereFile

            temp,ex = hereFile.rsplit('.',1)
            ex='.'+ex
            srcpath=os.path.join(root,hereFile)
            dstpath=root.replace(src,dst)+'/'

            if(ignoreList.has_key(ex)): #the extension is to be ignored
                continue
            elif(ignoreList.has_key(srcpath)):   #the file is to be ignored
                continue
            else:
                copyBasic(srcpath,dstpath)

    print '\n-----\nCopied\n-----\n'

