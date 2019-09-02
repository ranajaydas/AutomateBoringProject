""" Lots of fun image operations on the Oglaf comics from web_downloadoglaf.py """
import os
import numpy
import time
import threading
import re

os.chdir('./oglaf/unprocessed')                                     # change directory to ./oglaf/unprocessed
num_multi_threads = 10                                               # Specify number of threads for multi-threading


def count_comics(directory: str) -> int:
    """ Counts the number of files in a folder, divided by 3 """
    onlyfiles = next(os.walk(directory))[2]
    return int(len(onlyfiles)/3)


def split_list(input_list: list, n: int) -> list:
    """ Splits an input list into n parts"""
    return numpy.array_split(input_list, n)


def join_comics(comic_chunk):
    file_list = os.listdir(os.getcwd())
    not_found = []

    for comic_num in comic_chunk:
        title = str(comic_num) + '_title.gif'
        alttext = str(comic_num) + '_alttext.png'
        regex = re.compile('re.escape(comic_num)_(.*).jpg')
        for file in file_list:
            mo = regex.search(file)
            print(mo.group(1))

        if os.path.isfile(title) and os.path.isfile(alttext):
            print(alttext, title)


def multithread(files_to_process: list) -> None:
    """ Creates multiple threads of download based on an input split list of comics """
    process_threads = []                                               # List of all the Thread objects
    start_time = time.time()                                           # Timestamp start time

    # creates multiple threads and start downloading
    for process_chunk in files_to_process:                             # Iterate the split list chunk by chunk
        process_thread = threading.Thread(target=join_comics, args=(process_chunk,))
        process_threads.append(process_thread)
        process_thread.start()

    # Wait for all threads to end.
    for process_thread in process_threads:
        process_thread.join()

    end_time = time.time()                                             # Timestamp end time
    print('Operation completed in {} seconds.'.format(end_time - start_time))


comic_list = list(range(1, count_comics(os.getcwd())))
comic_list_split = split_list(comic_list, num_multi_threads)
multithread(comic_list_split)
