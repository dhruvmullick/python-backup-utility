"""
Python file backup utility
1. Copy files from src to dst
"""

import os;
import shutil, errno
import copyfiles

user="dhruvmullick"
# "src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/python-backup-utility/main.py"
src = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/"
dst = "/Users/dhruvmullick/CS/Project Work/python-backup-utility/destFolder/"

ignoreList = {".pdf":1} #write paths of files, extensions here which we don't want to copy
# ignoreList = {"/Users/dhruvmullick/CS/Project Work/python-backup-utility/srcFolder/gaddaarChetan.py":1}
# ignoreList={}

# copyfiles.myCopy1(src,dst)
copyfiles.myCopy2(src,dst,ignoreList)