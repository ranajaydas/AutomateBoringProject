"""Downloads every single sexylosers comic."""
import requests
import os
import bs4
import threading
import time                                                         # Used for calculating time spent downloading
import numpy                                                        # Used for splitting a list


os.makedirs('sexylosers', exist_ok=True)                            # Store comics in ./sexylosers
os.chdir('./sexylosers')                                            # change directory to ./sexylosers
latest_comic = 285                                                  # The latest comic number available online
num_multi_threads = 5                                               # Specify number of threads for multi-threading


def list_pending_files(last_comic: int) -> list:
    """Returns a list of .jpg files pending download."""
    pending_files = [str(num).zfill(3)                                                 # List Generator (3 digit format)
                     for num in range(1, last_comic+1)
                     if not (os.path.isfile(str("{0:0=3d}".format(num)) + '.jpg'))]    # Check if the file exists
    return pending_files


def split_list(input_list: list, n: int) -> list:
    """Splits an input list into n parts."""
    return numpy.array_split(input_list, n)


def download_sexylosers(comic_list: list) -> None:
    """Initiates a download from sexylosers.com for a list of comics."""
    base_url = 'https://sexylosers.com/comic/'                           # Starting URL

    for comic_num in comic_list:
        if not(os.path.isfile(comic_num + '.jpg')):                     # Check if comic already exists
            url = base_url + comic_num
            print('Downloading page {}...'.format(url))
            res = requests.get(url)                                     # Downloads the entire URL into res
            res.raise_for_status()                                      # Raises exception if the download has problems

            soup = bs4.BeautifulSoup(res.text, features="html.parser")  # Create a BeautifulSoup object

            # Find the URL of the comic image.
            comic_elem = soup.select('p img')                           # The comic image is store in a p tag

            if not comic_elem:
                print('Could not find comic image.')
            else:
                comic_url = comic_elem[0].get('src')                    # Find the comic image's URL
                print('Downloading image {}...'.format(comic_url))
                res = requests.get(comic_url)                           # Download the image.
                res.raise_for_status()

                # Save the image to ./sexylosers.
                image_file = open(os.path.join(str(comic_num) + '.jpg'), 'wb')
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
                image_file.close()


def multithread(files_to_download: list) -> None:
    """Creates multiple threads of download based on an input split list of comics."""
    download_threads = []                                               # List of all the Thread objects
    start_time = time.time()                                            # Timestamp start time

    # creates multiple threads and start downloading
    for download_chunk in files_to_download:                            # Iterate the split list chunk by chunk
        download_thread = threading.Thread(target=download_sexylosers, args=(download_chunk,))
        download_threads.append(download_thread)
        download_thread.start()

    # Wait for all threads to end.
    for download_thread in download_threads:
        download_thread.join()

    end_time = time.time()                                              # Timestamp end time
    print('Operation completed in {} seconds.'.format(end_time - start_time))


def check_missing(last_comic: int) -> list:
    """Checks for any missing files."""
    pending_downloads = list_pending_files(last_comic)                  # Check for missing files
    if pending_downloads:
        print('The following comics were not downloaded:\n', pending_downloads)
    else:
        print('All comics successfully downloaded!\n')
    return pending_downloads


def initiate(last_comic: int, num_threads: int) -> None:
    """Initiates the checking and download process."""
    files_to_download = list_pending_files(last_comic)                  # Create a list of files to be downloaded
    files_to_download = split_list(files_to_download, num_threads)      # Split the list based on number of threads
    multithread(files_to_download)                                      # Initiate multi-threaded download
    missing_files = check_missing(last_comic)                           # Check for any missing files
    if missing_files:
        initiate(last_comic, num_threads)                               # Recursive loop until all files downloaded


def main():
    initiate(latest_comic, num_multi_threads)                               # The ON switch!
    key_press = input("Press 'Y' to open the comics folder:")
    if key_press.lower() == 'y':
        os.startfile(os.getcwd())                                           # Open the comics folder


if __name__ == '__main__':
    main()
