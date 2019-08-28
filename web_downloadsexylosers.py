"""Downloads every single sexylosers comic."""
import requests
import os
import bs4

base_url = 'http://sexylosers.com/comic/'                      # starting url
last_comic_num = 285                                           # starting comic number
os.makedirs('sexylosers', exist_ok=True)                       # store comics in ./sexylosers

for i in range(last_comic_num, 0, -1):
    comic_num = ("{0:0=3d}".format(i))                         # uses 3 digits for the comic url number
    url = base_url + comic_num

    print('Downloading page {}...'.format(url))
    res = requests.get(url)                                    # Download the url
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select('p img')

    if not comic_elem:
        print('Could not find comic image.')
    else:
        comic_url = comic_elem[0].get('src')
        print('Downloading image {}...'.format(comic_url))
        res = requests.get(comic_url)                # Download the image.
        res.raise_for_status()

        # Save the image to ./sexylosers.
        image_file = open(os.path.join('sexylosers', str(comic_num) + '.jpg'), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

print('Done!')
