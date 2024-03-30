import os

folder = os.path.abspath('.')
print(folder)
biggestFile = 0
biggestFileName = ""
largeFiles = []
for foldernames, subfolders, filenames in os.walk(folder):
    for subfolder in subfolders:
        folder_and_subfolders = os.path.join(foldernames, subfolder)
        for filename in filenames:
            filename_path = os.path.join(folder_and_subfolders, filename)
            try:
                size = os.path.getsize(filename_path)
                if size > biggestFile:
                    biggestFile = size
                    biggestFileName = filename_path
                    largeFiles.append((biggestFileName, size))
            except:
                continue

print(largeFiles)

#learn how to check subfolders
#find the folder with the most files
#put it in a dictionary so you can see the top 10