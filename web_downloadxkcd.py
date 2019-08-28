"""Downloads every single XKCD comic."""
import requests
import os
import bs4

url = 'http://xkcd.com'                             # starting url
os.makedirs('xkcd', exist_ok=True)                  # store comics in ./xkcd

while not url.endswith('#'):
    print('Downloading page {}...'.format(url))
    res = requests.get(url)                         # Download the url
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if not comic_elem:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        print('Downloading image {}...'.format(comic_url))
        res = requests.get(comic_url)                # Download the image.
        res.raise_for_status()

        # Save the image to ./xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done!')
