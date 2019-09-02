"""Downloads every single Oglaf comic."""

import requests
import os
import bs4
from PIL import Image, ImageDraw, ImageFont


url = 'https://oglaf.com/cumsprite'                             # Starting URL...I'm serious
os.makedirs('oglaf', exist_ok=True)                             # Store comics in ./oglaf
os.chdir('./oglaf')                                             # change directory to ./oglaf
counter = 1


def save_alttext(alttext_name: str, alttext_value: str) -> None:
    fonts_folder = 'C:\\Windows\\Fonts'
    arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'arial.ttf'), 14)

    im = Image.new('RGBA', (760, 50), (204, 204, 204, 255))
    draw = ImageDraw.Draw(im)
    draw.text((20, 20), alttext_value, fill=(59, 67, 80, 255), font=arial_font)
    im.save(alttext_name)


def save_image(filename: str, img_url: str) -> None:
    if not (os.path.isfile(filename)):  # Check if the file already exists
        print('Downloading image {}...'.format(img_url))
        res = requests.get(img_url)  # Download the image.
        res.raise_for_status()

        # Save the image to ./oglaf
        image_file = open(filename, 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()


while True:
    print('Downloading page {}...'.format(url))
    res = requests.get(url)                                     # Download the URL
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select('b img')
    title_elem = soup.select('div img')

    if not comic_elem:
        print('Could not find comic image.')
    elif not title_elem:
        print('Could not find title image.')
    else:
        comic_url = comic_elem[0].get('src')                    # Get the comic's URL
        title_url = title_elem[2].get('src')                    # Get the title image's URL
        alttext_value = comic_elem[0].get('alt')                # Get the comic alt text

        title_name = str(counter) + '_title.gif'
        comic_name = str(counter) + '_' + os.path.basename(comic_url)
        alttext_name = str(counter) + '_alttext.png'

        save_image(comic_name, comic_url)
        save_image(title_name, title_url)
        if alttext_value:
            save_alttext(alttext_name, alttext_value)
        else:
            save_alttext(alttext_name, 'No alttext for this gem of a comic')

    # Get the Prev button's url.
    try:
        next_link = soup.select('a[rel="next"]')[0]
    except IndexError as err:
        print('Reached final page.')
        break
    url = 'https://oglaf.com' + next_link.get('href')
    counter += 1

print('Done!')
