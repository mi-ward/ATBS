import os

folder = os.path.abspath('/Users/michael')
for root, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        full_file_path = os.path.join(root, filename)
        if not os.path.islink(full_file_path) and os.path.getsize(full_file_path) >= 100000000:
            print(full_file_path, os.path.getsize(full_file_path))



            
            
            
        
