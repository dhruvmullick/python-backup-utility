# python-backup-utility

A utility to backup files and folders

1. Keep exceptions for backing up
2. Backup only the modified files (TO DO)
3. Create an ISO image after the backup is completed
4. Support extracting of backup files from ISO image (TO DO)

—————————————————————————————————————————————————————

Backend:


We take as input the source and destination from the user, and create a backup. The source may be either a:
  1. File
  2. Folder

The corner cases have been handled, such as :
  1. If the src is a file, then we must ensure that the destination folder exists. If it doesn't, then create it.
  2. If the src is a folder, then we must ensure that the destination folder does not exist. In such a case, we throw an error to the user to prevent overwriting valuable data.

Moreover, the user has the option to specify a list of :
  1. Files
  2. Folders
  3. Extensions
that he wishes to ignore. These would not be included in the backup.

To create an iso image of the backup, the user specifies the destination folder of the backup iso image. The iso image created is of the name ‘Backup_<time>_<date>’.

—————————————————————————————————————————————————————


Frontend :






—————————————————————————————————————————————————————
