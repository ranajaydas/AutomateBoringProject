"""Lots of fun image operations on the Oglaf comics from web_downloadoglaf.py"""
import os
import numpy
import time
import threading
from PIL import Image
from multiprocessing import Process

if not str(os.getcwd()).endswith('unprocessed'):
    os.chdir('./oglaf/unprocessed')                                 # change directory to ./oglaf/unprocessed
num_multi_threads = 15                                              # Specify number of threads for multi-threading
use_multiprocess = True                                             # Decide whether or not to use multi-processing
num_multi_process = 10                                               # Specify number of processes for multi-processing


def count_comics(directory: str) -> int:
    """Counts the number of files in a folder, divided by 3."""
    onlyfiles = next(os.walk(directory))[2]
    return int(len(onlyfiles)/3)


def split_list(input_list: list, n: int) -> list:
    """Splits an input list into n parts."""
    return numpy.array_split(input_list, n)


def join_comics(comic_chunk) -> None:
    """Joins the comic title, comic and alttext images and resizes them."""
    file_list = os.listdir(os.getcwd())

    for comic_num in comic_chunk:
        # Store the names for the Title, Comic and Alttext into variables
        prefix = str(comic_num) + '_'
        title = prefix + 'title.gif'
        alttext = prefix + 'alttext.png'

        for file in file_list:
            if file.startswith(prefix) and file.endswith('.jpg'):
                comic = file
                comic_text_only = file.split('.')[0]

        # Create a collage image
        print('Creating collage for {}...'.format(comic_text_only))
        collage_img = Image.new('RGB', (800, 680), (204, 204, 204, 255))       # Create a blank image
        title_img = Image.open(title)
        comic_img = Image.open(comic)
        alttext_img = Image.open(alttext)
        collage_img.paste(title_img, (20, 5))
        collage_img.paste(comic_img, (20, 36))
        collage_img.paste(alttext_img, (20, 632))

        # Resize the collage image and save it
        print('Resizing {}...'.format(comic_text_only))
        final_img = collage_img.resize((1200, 1020), Image.ANTIALIAS)
        final_img.save('../' + comic_text_only + '_PROCESSED.jpg')


def multithread(files_to_process: list) -> None:
    """Creates multiple threads of download based on an input split list of comics."""
    process_threads = []                                               # List of all the Thread objects

    # creates multiple threads and start downloading
    for process_chunk in files_to_process:                             # Iterate the split list chunk by chunk
        process_thread = threading.Thread(target=join_comics, args=(process_chunk,))
        process_threads.append(process_thread)
        process_thread.start()

    # Wait for all threads to end.
    for process_thread in process_threads:
        process_thread.join()


def multiprocess(files_to_process: list) -> None:
    """Creates multiple processes based on an input split list of comics."""
    processes = []                                               # List of all the multi-process objects

    # creates multiple processes
    for process_chunk in files_to_process:                             # Iterate the split list chunk by chunk
        process = Process(target=multithread, args=(process_chunk,))
        processes.append(process)
        process.start()

    # Wait for all threads to end.
    for process in processes:
        process.join()


def main():
    comic_list = list(range(1, count_comics(os.getcwd())+1))
    comic_list_split1 = split_list(comic_list, num_multi_threads)
    if use_multiprocess:
        comic_list_split2 = split_list(comic_list_split1, num_multi_process)
        multiprocess(comic_list_split2)
    else:
        multithread(comic_list_split1)


if __name__ == '__main__':
    start_time = time.time()                                           # Timestamp start time
    main()
    end_time = time.time()                                             # Timestamp end time
    print('Operation completed in {} seconds.'.format(end_time - start_time))
