"""
Python file backup utility
1. Copy files from src to dst
"""

import os
import shutil, errno
import copyfiles
import datetime


# "src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/python-backup-utility/main.py"
src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/"
dst = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/destFolder/"

# ignoreList = {".pdf":1} #write paths of files, folders and extensions here which we don't want to copy
# ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/gaddaarChetan.py":1}
ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/Bleh":1}
# ignoreList={}

# copyfiles.myCopy1(src,dst)
copyfiles.myCopy2(src,dst,ignoreList)

#create an isoimage of the backup folder

now = datetime.datetime.now()

isodstfolder = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/"    #folder where iso image is to be saved. Take input from user.
backupdst=dst   #folder of which we have to make backup

print isodstfolder
print backupdst

fname = "Backup_%s-%s-%s-%s-%s.iso" %(now.hour,now.minute,now.day,now.month,now.year)   #name of iso image
isodst=os.path.join(isodstfolder,fname)

os.system("mkisofs -o '%s' '%s'" %(isodst,backupdst))

print "\n\nBackup has been created successfully. Thank you. \n\n"