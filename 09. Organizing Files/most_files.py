import os

folder = os.path.abspath('.')

folder_dict = {}
file_quantity = 0
largest_file = ""

for foldernames, subfolders, filenames in os.walk(folder):
    if len(filenames) > file_quantity:
        file_quantity = len(filenames)
        largest_file = foldernames

print(largest_file, file_quantity)


