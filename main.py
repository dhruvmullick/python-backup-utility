"""
Python file backup utility
"""

import copyFiles
import createISO

# "src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/python-backup-utility/main.py"
src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/"
dst = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/destFolder/"

# ignoreList = {".pdf":1} #write paths of files, folders and extensions here which we don't want to copy
# ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/gaddaarChetan.py":1}
ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/Bleh":1}
# ignoreList={}

# copyfiles.copyBasic(src,dst)
copyFiles.copyFull(src,dst,ignoreList)

#create an isoimage of the backup folder
isodstfolder = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/"    #folder where iso image is to be saved. Take input from user.
backupdst=dst   #folder of which we have to make backup
createISO.isoCreator(backupdst,isodstfolder)

print "\n\nBackup has been created successfully. Thank you. \n\n"