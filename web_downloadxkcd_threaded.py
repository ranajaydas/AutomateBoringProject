"""Downloads a given range of XKCD comics using multi-threading"""
import requests
import os
import bs4
import threading


def xkcd_download(starting_comic: int, ending_comic: int) -> None:
    for urlnumber in range(starting_comic, ending_comic+1):
        if urlnumber == 404:                                                             # Skip comic #404
            continue
        print('Downloading page {}...'.format(urlnumber))
        res = requests.get('http://xkcd.com/{}'.format(urlnumber))                       # Download the url
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Downloading image {}...'.format(comic_url))
            res = requests.get(comic_url)                                               # Download the image.
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


os.makedirs('xkcd', exist_ok=True)                                                      # store comics in ./xkcd
first_comic = 1                                                                         # First comic to download
last_comic = 1000                                                                       # Last comic to download

# Create and start the Thread objects.
download_threads = []                                                                   # list of all the Thread objects
for i in range(first_comic, last_comic, 100):                                           # creates multiple threads
    download_thread = threading.Thread(target=xkcd_download, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()
print('Done.')
