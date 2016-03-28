"""
Python file backup utility
"""

import diffBackup
import createISO
import clean

# "src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/python-backup-utility/main.py"
# src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/"
# dst = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/destFolder/"


# ignoreList = {".pdf":1} #write paths of files, folders and extensions here which we don't want to copy
# ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/gaddaarChetan.py":1}
# ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/MyFolder":1}
# ignoreList={}


def backupNow(L,dst, ignoreList):

    # Make a completely fresh backup
    #delete the files already there at dst, as this is a fresh backup.
    #
    # clean.readyDst(dst)
    # copyFiles.copyFull(src,dst,ignoreList)

    # Make a differential backup

    for src in L:
        print src
    print dst

        # diffBackup.mainDiffBackup(src,dst,ignoreList)

    # Create an isoimage of the backup folder
    # isodstfolder = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/"    #folder where iso image is to be saved. Take input from user.
    # backupdst=dst   # Folder of which we have to make backup
    # createISO.isoCreator(backupdst,isodstfolder)
    print "\n\nBackup has been created successfully. Thank you. \n\n"


    for src in L:
        print src
    print dst
