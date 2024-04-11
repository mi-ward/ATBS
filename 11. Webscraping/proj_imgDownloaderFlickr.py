from bs4 import BeautifulSoup
import os, sys, requests

search_term = sys.argv[1]
url = 'https://www.flickr.com/search/?text='
folder_name = search_term + " images"
os.makedirs(folder_name, exist_ok=True)

res = requests.get(url+search_term)
res.raise_for_status
soup = BeautifulSoup(res.content,'html.parser')

img_list = soup.find_all('img')

for image in img_list:
    if image.get('src').startswith('https:'):
        continue
    
    image_url = 'https:' + image.get('src')
    res = requests.get(image_url)
    res.raise_for_status
    print(res.headers)
    print(res.status_code)

    print(image_url)
    print("Downloading: ", os.path.join(folder_name, os.path.basename(image_url)))
    image_file = open(os.path.join(folder_name, os.path.basename(image_url)), 'wb')
    

    for chunk in res.iter_content(100000):
        image_file.write(chunk)

    image_file.close()


    






