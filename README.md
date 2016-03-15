# python-backup-utility
A utility to backup files and folders

1. Keep exceptions for backing up
2. Backup only the modified files (TO DO) 
3. Create an ISO image after the backup is completed 

—————————————————————————————————————————————————————

Backend: 


We take as input the source and destination from the user, and create a backup. The source may be either a:
  1. File
  2. Folder

Moreover, the user has the option to specify a list of :
  1. Files
  2. Folders
  3. Extensions 
that he wishes to ignore. These would not be included in the backup.

To create an iso image of the backup, the user specifies the destination folder of the backup iso image. The iso image created is of the name ‘Backup_<time>_<date>’. 

—————————————————————————————————————————————————————


Frontend : 






—————————————————————————————————————————————————————
