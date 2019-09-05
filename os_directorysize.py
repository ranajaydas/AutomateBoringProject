"""Prints the total size of all the files in a specified path."""

import os

total_size = 0
directory_name = 'D:\\Installation Files'

for filename in os.listdir(directory_name):
    total_size += os.path.getsize(os.path.join(directory_name, filename))

print('{} bytes'.format(total_size))
print('or {0:.2f} GB'.format(total_size/1073741824))
