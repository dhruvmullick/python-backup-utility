import shutil, errno
import os

#myCopy1 - Recursive copy. src can be a folder or a file, and dst path shouldn't exist is folder copied, but doesn't matter if file copied
#better than the default copy2() function, as we can specify the new filename as well.
def myCopy1(src,dst):
    if os.path.isfile(src): #src is a file.
        print "lullz"
        if not os.path.exists(dst): #if it is a file then dst folder must exist
            os.mkdir(dst)
        # L=src.rsplit('.',1) #obtain the source and dest path
        # L[0]=L[0]+'_new'      #use this to keep a new name for the copied file
        # src=L[0]+'.'+L[1]
        dst=dst+os.path.basename(src)  #copy src file with a new name to dst folder
        shutil.copyfile(src,dst)
        return
    try:
        print "meh"
        shutil.copytree(src, dst)   #copy entire directory. dst directory shouldn't exist already
    except OSError as exc:  #if it is a file. But this doesn't change the name of the file to a new name. So we have created our own function above
         print "lol"
    #     if exc.errno == errno.ENOTDIR:
    #         shutil.copy2(src, dst)
    #     else:
    #         raise
    #

#myCopy2 - copy files from src to dst recursively. If the file is an exception, then ignore it.

def myCopy2(src, dst, ignoreList):

    notenter="/User/!/~"  #a string which can never be possible
    for root,dirs,files in os.walk(src):   #walk through the directory

        root = root+'/' #important to have this '/' here for the ignore list, as otherwise, folder name like "Bleh2" would also get ignored along with "Bleh" as substring search would give true for it too.
        os.chdir(root)
        if ignoreList.has_key(root):
            notenter=root
            continue

        if notenter in root:
            continue

        print 'root = ' + root

        for hereFiles in files:
            if(hereFiles[0]=='.'):   #don't copy hidden files
                continue

            print 'file name = ' + hereFiles

            temp,ex = hereFiles.rsplit('.',1)
            ex='.'+ex
            srcpath=os.path.join(root,hereFiles)
            dstpath=root.replace(src,dst)+'/'

            if(ignoreList.has_key(ex)): #the extension is to be ignored
                continue
            elif(ignoreList.has_key(srcpath)):   #the file is to be ignored
                continue
            else:
                print 'srcpath = ' + srcpath
                print 'dstpath = ' + dstpath
                myCopy1(srcpath,dstpath)
                print 'Copied\n'
