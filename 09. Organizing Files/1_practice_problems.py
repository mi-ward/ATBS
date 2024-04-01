# 1. What is the difference between shutil.copy() and shutil.copytree()?
    # shutil.copy() copies the single file/folder but copytree includes the entire file tree underneath
# 2. What function is used to rename files?
    # shutil.move()
# 3. What is the difference between the delete functions in the send2trash and shutil modules?
    # send2trash will send the deleted file to the trash, delete in shutil will just outright delete the file
# 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
    # zipfile.ZipFile("file", 'w')
