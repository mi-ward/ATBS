# To add a prefix to the start of the filename, such as adding spam_ to rename eggs.txt to spam_eggs.txt

import os, shutil

# Define the prefix
prefix = "spam"


# Navigate to the folder
files = os.listdir(".")
for file in files:
    absPath = os.path.abspath("./%s" % file)
    if absPath != __file__:
        directory = os.path.dirname(absPath)
        newFilePath = os.path.join(directory, (prefix + "_" + file))
        shutil.move(absPath, newFilePath)
        

