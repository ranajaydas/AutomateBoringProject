"""Downloads every single sexylosers comic."""
import requests
import os
import bs4
import threading
import time
import numpy

os.makedirs('sexylosers', exist_ok=True)                            # store comics in ./sexylosers
os.chdir('./sexylosers')                                            # change directory to ./sexylosers
latest_comic = 285                                                  # The latest comic number available online
num_threads = 5                                                     # specify the number of threads for multithreading


def list_pending_files(last_comic: int) -> list:
    """ Returns a list of .jpg files pending download """
    pending_files = [str("{0:0=3d}".format(num))
                     for num in range(1, last_comic+1)
                     if not (os.path.isfile(str("{0:0=3d}".format(num)) + '.jpg'))]
    return pending_files


def split_list(input_list: list, n: int) -> list:
    """ Splits an input list into n parts"""
    return numpy.array_split(input_list, n)


def download_sexylosers(comic_list: list) -> None:
    """ Initiates a download from sexylosers.com"""
    base_url = 'http://sexylosers.com/comic/'                           # starting url

    for comic_num in comic_list:
        if not(os.path.isfile(comic_num + '.jpg')):                     # Check if comic already exists
            url = base_url + comic_num
            print('Downloading page {}...'.format(url))
            res = requests.get(url)                                     # Download the url
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, features="html.parser")

            # Find the URL of the comic image.
            comic_elem = soup.select('p img')

            if not comic_elem:
                print('Could not find comic image.')
            else:
                comic_url = comic_elem[0].get('src')
                print('Downloading image {}...'.format(comic_url))
                res = requests.get(comic_url)                           # Download the image.
                res.raise_for_status()

                # Save the image to ./sexylosers.
                image_file = open(os.path.join(str(comic_num) + '.jpg'), 'wb')
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
                image_file.close()


files_to_download = list_pending_files(latest_comic)
files_to_download = split_list(files_to_download, num_threads)
download_threads = []                                                 # list of all the Thread objects
start_time = time.time()                                              # Timestamp start time
for download_chunk in files_to_download:                              # creates multiple threads
    download_thread = threading.Thread(target=download_sexylosers, args=list(download_chunk))
    download_threads.append(download_thread)
    download_thread.start()
    print(download_chunk)

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()

end_time = time.time()                                               # Timestamp end time
print('Operation completed in {} seconds.'.format(end_time-start_time))
