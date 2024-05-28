#Scheduled Web Comic Downloader
#Write a program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit. 
#Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on macOS, and cron on Linux) can run your Python program once a day. 
#The Python program itself can download the comic and then copy it to your desktop so that it is easy to find. 
#This will free you from having to check the website yourself to see whether it has updated. 
#(A list of web comics is available at https://nostarch.com/automatestuff2/.)


import os, requests, bs4

FOLDER = {
        'xkcd': 'https://xkcd.com/',
        'Perry Bible Fellowship': 'https://pbfcomics.com/'
        }


def getDailyComic(url, folder):
    exists = False
    res = requests.get(url)
    print('Downlading page %s...' % (url))
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    comic = soup.select('#comic img')
    if comic == []:
        print('No comic')
    else:
        comicUrl = comic[-1].get('src')
        print('Downloading image %s...' % (comicUrl))
        
        if comicUrl.startswith('https:'):
            res = requests.get(comicUrl)
        else:
            res = requests.get('https:' + comicUrl)
        
        res.raise_for_status()
        
        #if file already exists, ignore else create the new image
        
        for dir in os.walk('.'):
            if os.path.basename(comicUrl) in dir[2]:
                print('File already exists.')
                exists = True
        
        if exists == False:    
            imageFile = open(os.path.join(folder, os.path.basename(comicUrl)), 'wb')
        
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        
for folderName, url in FOLDER.items():
    os.makedirs(folderName, exist_ok=True)
    getDailyComic(url, folderName)
    
            
    
