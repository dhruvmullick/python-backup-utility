"""
To create an iso image of the backup folder
Note that mkisofs must be installed on the system. Note that this is not on windows.
"""

import datetime
import os

#take as input the destination of the source folder, i.e. where the backup was created, and the iso destination folder

def isoCreator(backupdst,isodstfolder):
    print "iso"
    print backupdst
    print isodstfolder

    now = datetime.datetime.now()
    fname = "Backup_%s-%s_%s-%s-%s.iso" %(now.hour,now.minute,now.day,now.month,now.year)   #name of iso image
    isodst=os.path.join(isodstfolder,fname)
    os.system("mkisofs -o '%s' '%s'" %(isodst,backupdst))

