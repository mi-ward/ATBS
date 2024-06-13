#! python3
# Import modules and write comments to describe this program.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/Users'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        fn, ext = os.path.splitext(filename)
        if ext.lower() not in ['.png', 'jpg']:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im = Image.open(os.path.join(foldername, filename))
        width, height = im.size
        # Check if width & height are larger than 500.
        if (width >= 500 and height >= 500):
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))