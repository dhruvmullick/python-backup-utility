Python Backup Utility
========================

A utility to backup files and folders

1. Keep exceptions for backing up
2. Incremental Backup (Backup only the modified files)
3. Show history of files backed up / deleted. 
3. Create an ISO image after the backup is completed
4. Support extracting of backup files from ISO image (TO DO)
    
__________


System Requirements: 
----

  1. Unix based system 
  2. Python >=2.7 
  3. mkisofs installed (Only if you want to make an ISO image) 



How to Use: 
---

  1. Run GUI.py
  2. Select files to be backed up, backup destination in GUI window. 
  3. (Optional) In the Ignore Tab, select the files/folders or extension to be ignored while backing up.
  4. (Optional) In the ISO image tab, select the destination path for the ISO image.


Backend:
---------

We take as input the source and destination from the user, and create a backup. The source may be either a:
  1. File
  2. Folder

The user has the option to specify a list of :
  1. Files
  2. Folders
  3. Extensions
that he wishes to ignore. These would not be included in the backup.

Incremental Backup :  
  1. Modified and Added files are copied from source to dest
  2. Files deleted from source are removed from dest 


To create an iso image of the backup, the user specifies the destination folder of the backup iso image. The iso image created is of the name ‘Backup_<time>_<date>’. 


__________


Frontend :
-----------

Used Tkinter. 



