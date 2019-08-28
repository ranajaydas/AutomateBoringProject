""" A program that takes backups of a specified directory and auto-increments the backup number """

import os
import zipfile
from datetime import date

folder_to_backup = 'C:\\Users\\Ranaj\\Documents\\Dropbox\\Learning\\' \
                   'Python\\Automate The Boring Stuff\\AutomateBoringProject\\Quiz'


def backuptozip(folder_name :str) ->None:
    folder_name = os.path.abspath(folder_name)         # make sure folder is absolute
    date_today = str(date.today())                     # create a variable containing today's date
    number = 1                                         # postfix to be added to filename
    os.chdir(os.path.join(folder_name, '..'))          # change the current working directory to parent directory

    # Create a unique zipfile name
    while True:
        zipfile_name = 'zip_' + os.path.basename(folder_name) + '_' + str(number) + '_' + date_today + '.zip'
        if not os.path.exists(zipfile_name):           # check if the file exists
            break
        number += 1                                    # increment the number if the file exists

    # Create the zip file
    print('Creating {} in {} ...'.format(zipfile_name, os.getcwd()))
    backup_zipfile = zipfile.ZipFile(zipfile_name, 'w')                 # creates an empty zipfile

    # Walk through all the files and folders inside
    for foldername, subfolders, filenames in os.walk(folder_name):
        print('Adding files in {} ...', foldername)

        # need to add this to prevent incorrect folders (copied from reddit)
        arcname = foldername[len(folder_name) - len(os.path.basename(folder_name)):]

        backup_zipfile.write(foldername, arcname)                       # add the current folder to the zipfile

        for filename in filenames:                                      # add all the files in the folder to the zipfile
            new_base = os.path.basename(folder_name) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue                                                # skips backing up the zip file itself
            full_path = os.path.join(foldername, filename)

            # need to add this to prevent incorrect folders (copied from reddit)
            arcname = full_path[len(folder_name) - len(os.path.basename(folder_name)):]

            backup_zipfile.write(full_path, arcname)

    backup_zipfile.close()
    print('Done!')


# Call the backup zipfile function
backuptozip(folder_to_backup)
