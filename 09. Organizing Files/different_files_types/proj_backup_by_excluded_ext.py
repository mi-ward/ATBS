import os, sys, zipfile

wd = os.getcwd()

print(wd)

ext = sys.argv[1]
zipFilename = ("Archive_of_non_%s_files" % ext) + '.zip'
backupFile = zipfile.ZipFile(zipFilename, 'w')

for foldername, subfolders, files in os.walk(os.path.abspath('.')):
    backupFile.write(foldername)

    for filename in files:
        if not filename.endswith(ext) and filename != os.path.basename(__file__) and not filename.endswith('.zip'):
            backupFile.write(os.path.join(foldername, filename))
            #print(foldername)
            print(os.path.join(foldername, filename))

backupFile.close()
