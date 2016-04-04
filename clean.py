"""
Prepare the destination folder for backup. Delete the pre existing files there.
"""

import os
import shutil

def readyDst(dst):
    if os.path.isfile(dst):
        os.remove(dst)
        print("%s File deleted" %(os.path.basename(dst)))
    elif os.path.isdir(dst):
        shutil.rmtree(dst)
        print("%s Directory deleted" %dst)

