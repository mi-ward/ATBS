import os, shutil, re

#define regex

pattern = re.compile(r'0')

files = os.listdir()

for file in files:
    fileZerosRemoved = re.sub(pattern, "", file)
    fileAbsPath = os.path.abspath(file)
    fileZerosRemovedAbsPath = os.path.join(os.path.dirname(fileAbsPath), fileZerosRemoved)
    if fileAbsPath != __file__:
        print(fileZerosRemovedAbsPath)
        shutil.move(fileAbsPath, fileZerosRemovedAbsPath)
    
    