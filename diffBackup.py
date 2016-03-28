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

#while making src dictionary, make sure to replace the src part with dst. Because we'll be checking if the dst dict item is present in the src dict
def srcDictGen(src,dst,ignoreList):

    srcFilesDict={}
    srcDirsDict={}
    if(ignoreList.has_key(src)):
        return (srcFilesDict,srcDirsDict)

    for root,dirs,files in os.walk(src):   #walk through the directory

        dirs[:] = [d for d in dirs if os.path.join(root,d) not in ignoreList] #modify dirs so that you enter only if the subdirectory is not in ignoreList
        os.chdir(root)

        for d in dirs:
            srcDirsDict[os.path.join(root,d).replace(src,dst)]=1   #srcDirsDict must store the address we need in the dst directory

        for hereFile in files:
            if(hereFile[0]=='.'):   #don't copy hidden files
                continue

            temp,ex = hereFile.rsplit('.',1)
            ex='.'+ex
            srcpath=os.path.join(root,hereFile)
            dstpath=root.replace(src,dst)+'/'

            if(ignoreList.has_key(ex)): #the extension is to be ignored
                continue
            elif(ignoreList.has_key(srcpath)):   #the file is to be ignored
                continue
            else:
                filepath =  srcpath
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
                # v = time.ctime(mtime)
                srcFilesDict[filepath.replace(src,dst)]=mtime

    return (srcFilesDict,srcDirsDict)

def dictGen(src,dst,ignoreList):

    dstFilesDict={}
    dstDirsDict={}

    srcFilesDict,srcDirsDict=srcDictGen(src,dst,ignoreList)

    for root,dirs,files in os.walk(dst):
        for hereFile in files:
            if hereFile[0] == '.': #hidden files
                continue
            filepath =  os.path.join(root,hereFile)
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
            # v = time.ctime(mtime)
            dstFilesDict[filepath]=mtime
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

    # delete the files
    for file in rem:
        if os.path.isfile(file):
            os.remove(file)
            print("%s file deleted" %(os.path.basename(file)))
        else:
            print("Error: %s file not found" % file)


def delOldFolders(srcDirsDict,dstDirsDict):

    # make a list of folders which are no longer in src and delete them (we would have already deleted the files in it)
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
    #make a list of the modified/new files
    for hereFile in srcFilesDict:
        if hereFile not in dstFilesDict:    #it is a new file
            mod += [hereFile]
        elif srcFilesDict[hereFile]>dstFilesDict[hereFile]: #that is the source file is more recent
            mod += [hereFile]

    #copy the files in the list
    for hereFile in mod:
        hereFileDst=os.path.dirname(hereFile)+'/'
        hereFileSrc=hereFile.replace(dst,src)   #as we had modified the source file path
        copyFiles.copyBasic(hereFileSrc,hereFileDst)
        print '%s file created' % os.path.basename(hereFile)

# copy the new empty folders. The non empty folders would have been created already
def addNewEmptyFolders(srcDirsDict,dstDirsDict):

    mod = []
    for Dirs in srcDirsDict:
        if Dirs not in dstDirsDict:    #it is a new file
            mod += [Dirs]
    for Dirs in mod:
        if(not os.path.isdir(Dirs)):
            os.mkdir(Dirs)
            # print 'asdfasdfadsf'
            print '%s empty folder created' % Dirs

        # print '%s empty folder created' % os.path.basename(Dirs)


def mainDiffBackup(src, dst, ignoreList):

    srcFilesDict,dstFilesDict,srcDirsDict,dstDirsDict = dictGen(src,dst,ignoreList)
    delOldFiles(srcFilesDict,dstFilesDict)
    delOldFolders(srcDirsDict,dstDirsDict)  #which would now be empty after delOldFiles
    addModFiles(srcFilesDict,dstFilesDict,src,dst)
    addNewEmptyFolders(srcDirsDict,dstDirsDict)   #the new folders with new files would have been created already