"""
Differentially backup files from src to dst
"""

import os
import time
import shutil
import copyFiles

# generate dictionaries for src and dst files. {FilePath : Modification Time}
# generate dictionaries for src and dst directories. {FilePath : 1}. Needed because we may have to delete a folder altogether if it has been deleted from the src.
# But we can't do this solely on the basis of size=0 of dst, as the folder may be of size=0 in the src too. Hence keep track of src folders too. Just see the folder exists in the src as well.
# mtime is time the file's Contents were last changed (in Unix systems). ctime gives the time the file's metadata was changed.
# .ctime is method for formatting the string inside

def dictGen(src,dst):

    srcFilesDict={}
    dstFilesDict={}
    srcDirsDict={}
    dstDirsDict={}

    #while making src dictionary, make sure to replace the src part with dst. Because we'll be checking if the dst dict item is present in the src dict
    for root,dirs,files in os.walk(src):
        for hereFile in files:
            if hereFile == '.DS_Store': #mac problem
                continue
            filepath =  os.path.join(root,hereFile)
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
            v = time.ctime(mtime)
            srcFilesDict[filepath.replace(src,dst)]=v
        for hereDir in dirs:
            filepath =  os.path.join(root,hereDir)
            srcDirsDict[filepath.replace(src,dst)] = 1


    for root,dirs,files in os.walk(dst):
        for hereFile in files:
            if hereFile == '.DS_Store': #mac problem
                continue
            filepath =  os.path.join(root,hereFile)
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
            v = time.ctime(mtime)
            dstFilesDict[filepath]=v
        for hereDir in dirs:
            filepath =  os.path.join(root,hereDir)
            dstDirsDict[filepath] = 1

    return (srcFilesDict,dstFilesDict,srcDirsDict,dstDirsDict)


# Delete the files which are no longer in the source now.
def delOldFiles(srcFilesDict,dstFilesDict):

    # make a list of files which are no longer in src and delete them
    rem = []
    for file in dstFilesDict:
        if file not in srcFilesDict :
            rem += [file]

    for file in rem:
        if os.path.isfile(file):
            os.remove(file)
            print("%s file deleted" %(os.path.basename(file)))
        else:
            print("Error: %s file not found" % file)


def delOldFolders(srcDirsDict,dstDirsDict):

    # make a list of files which are no longer in src and delete them
    rem = []
    for Dir in dstDirsDict:
        if Dir not in srcDirsDict :
            rem += [Dir]

    for Dir in rem:
        try:
            shutil.rmtree(Dir)
            print("%s folder deleted" %(os.path.basename(Dir)))
        except OSError, e:
            print ("Error: %s - %s." % (e.filename,e.strerror))

def addModFiles(srcFilesDict,dstFilesDict,src,dst):

    mod = []
    for hereFile in srcFilesDict:
        if hereFile not in dstFilesDict:    #it is a new file
            mod += [hereFile]
        elif srcFilesDict[hereFile]>dstFilesDict[hereFile]:
            mod += [hereFile]

    for hereFile in mod:
        hereFileDst=os.path.dirname(hereFile)+'/'
        hereFileSrc=hereFile.replace(dst,src)   #as we had modified the source file path
        copyFiles.copyBasic(hereFileSrc,hereFileDst)
        print '%s file created' % os.path.basename(hereFile)

def addNewEmptyFolders(srcDirsDict,dstDirsDict):

    mod = []
    for Dirs in srcDirsDict:
        if Dirs not in dstDirsDict:    #it is a new file
            mod += [Dirs]
    for Dirs in mod:
        os.mkdir(Dirs)
        print '%s empty folder created' % os.path.basename(Dirs)


def mainDiffBackup(src, dst):

    srcFilesDict,dstFilesDict,srcDirsDict,dstDirsDict = dictGen(src,dst)
    delOldFiles(srcFilesDict,dstFilesDict)
    delOldFolders(srcDirsDict,dstDirsDict)
    addModFiles(srcFilesDict,dstFilesDict,src,dst)
    addNewEmptyFolders(srcDirsDict,dstDirsDict)   #the new folders with new files would have been created already









