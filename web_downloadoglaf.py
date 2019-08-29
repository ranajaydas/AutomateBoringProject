"""Downloads every single Oglaf comic."""

import requests
import os
import bs4

url = 'https://oglaf.com/cumsprite'                             # Starting URL...I'm serious
os.makedirs('oglaf', exist_ok=True)                             # Store comics in ./oglaf
os.chdir('./oglaf')                                             # change directory to ./oglaf
counter = 1

while True:
    print('Downloading page {}...'.format(url))
    res = requests.get(url)                                     # Download the URL
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select('b img')
    if not comic_elem:
        print('Could not find comic image.')
    else:
        comic_url = comic_elem[0].get('src')
        if not(os.path.isfile(os.path.basename(comic_url))):        # Check if the file already exists
            print('Downloading image {}...'.format(comic_url))
            res = requests.get(comic_url)                           # Download the image.
            res.raise_for_status()

            # Save the image to ./oglaf
            image_file = open(str(counter) + '_' + os.path.basename(comic_url), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

    # Get the Prev button's url.
    try:
        next_link = soup.select('a[rel="next"]')[0]
    except IndexError as err:
        print('Reached final page.')
        break
    url = 'https://oglaf.com' + next_link.get('href')
    counter += 1

print('Done!')
