#! python3
# luckygoogle - Opens the first 5 search results on Google for a search phrase

import webbrowser
import sys
import requests
import bs4


if len(sys.argv) > 1:
    # Get search term from command line.
    searchterm = ' '.join(sys.argv[1:])
else:
    # Get search term from user.
    searchterm = input('Enter the search term: ')


print('Googling...')
res = requests.get('http://google.com/search?q=' + searchterm)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Select the search result links which are found
linkelems = soup.select('div#main > div > div > div > a')

# Open a browser tab for each result.

webbrowser.open('http://google.com/search?q=' + searchterm)
numopen = min(5, len(linkelems))                                # choose whichever number is smaller
for i in range(numopen):
    webbrowser.open('http://google.com' + linkelems[i].get('href'))

