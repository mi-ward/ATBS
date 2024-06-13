#! python3

import os
from PIL import Image, ImageDraw, ImageFont

fo = open('guests.txt')
guests = fo.read().splitlines()    
fo.close()

fonts_folder = '/System/Library/Fonts'
font = ImageFont.truetype(os.path.join(fonts_folder, "NewYorkItalic.ttf"), 30)

for guest in guests:
    im = Image.new('RGBA', (288,360), 'white')
    width, height = im.size
    h_center = int(width/2)
    v_center = int(height/2)
    
    flowerIm = Image.open('flower.png')
    flowerIm = flowerIm.resize((width,height))
    im.paste(flowerIm,(0,0))
    draw = ImageDraw.Draw(im)
    draw.text((h_center, v_center+10), guest, fill="black", anchor="ms", align='center', font=font)
    
    
    
    im.save('place_setting_for_%s.png' % guest)
    



