"""
Python file backup utility
1. Copy files from src to dst
"""

import os;
import shutil, errno
import copyfiles

user="dhruvmullick"
# src = "/Users/%s/python-backup-utility/main.py" %(user)
src = "/Users/%s/python-backup-utility/srcFolder/" %(user)
dst = "/Users/%s/python-backup-utility/destFolder/" %(user)

ignoreList = {}

# copyfiles.myCopy1(src,dst)
copyfiles.myCopy2(src,dst,ignoreList)