import os, sys, zipfile

wd = os.getcwd()

ext = sys.argv[1]
zipFilename = ("Archive_of_%s_files" % ext) + '.zip'
backupFile = zipfile.ZipFile(zipFilename, 'w')

for foldername, subfolders, files in os.walk(os.path.abspath('.')):
    backupFile.write(foldername)

    for filename in files:
        if filename.endswith(ext) and filename != os.path.basename(__file__):
            backupFile.write(os.path.join(foldername, filename))

backupFile.close()
