"""Walks through all the files and subfolders in a specified path."""
import os

pathname = 'C:\\Intel'

for foldername, subfolders, filenames in os.walk(pathname):
    print('The current folder is:', foldername)

    for subfolder in subfolders:
        print('Subfolder of {}: {}'.format(foldername, subfolder))

    for filename in filenames:
        print('File inside {}: {}'.format(foldername, filename))
    print()
