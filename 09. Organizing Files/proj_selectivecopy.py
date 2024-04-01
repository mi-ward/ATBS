import os, shutil

ext = 'pdf'
new_dir_path = './all_%ss' % ext
os.mkdir(new_dir_path)

folder = os.path.abspath('../..')

for folders, subfolders, files in os.walk(folder):
    for file in files:
        filename = os.path.join(folders, file)

        if filename.endswith(ext):
            print('Adding %s to new folder.' % os.path.basename(filename))
            print(os.path.abspath(new_dir_path))
            try:
                shutil.copy(os.path.abspath(filename), os.path.abspath(new_dir_path))
            except shutil.SameFileError:
                print('File already copied')
                
            

