from bs4 import BeautifulSoup
import os, requests, sys

url = sys.argv[1]
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
print(res.content)
folder_name = 'site-links'

os.makedirs(folder_name, exist_ok=True)

links = set(map(lambda a: a.get('href'), soup.find_all('a')))

def download_site(url):
    res = requests.get(url)
    status_code = res.status_code
    
    if status_code != 200:
        print(status_code)
    else:
        try:
            #url = url.lstrip('https:/')
            site_file = open(os.path.join(folder_name, (os.path.basename(url) + '.html')), 'wb')
            site_file.write(res.content)
            site_file.close()
        except:
            print("duplicate @", url)



for link in links:
    if link is None or not link.startswith('http'):
        print("No link available at %s" % link)
    else:
        download_site(link)
        