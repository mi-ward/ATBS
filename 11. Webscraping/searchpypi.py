#! python3
#searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...')  #display text while downloading search results page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve the top search result link.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening ', urlToOpen)
    webbrowser.open(urlToOpen)
