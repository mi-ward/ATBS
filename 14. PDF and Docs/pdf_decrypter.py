#! python3

import os
import PyPDF2
import sys
from send2trash import send2trash

# get the password
pw = sys.argv[2]

#dir = sys.argv[1]
dir = os.path.abspath('.') 
print(dir)

for root, dirs, files in os.walk(os.path.join(dir, "PDFs_To_Encrypt")):
    for file in files:
        if file.endswith('.pdf'):
            oldPath = os.path.join(root, file)
            pdfFile = open(oldPath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            if pdfReader.isEncrypted:
                try:
                    pdfReader.decrypt(pw)
                except:
                    print('could not decrypt file')
            else:
                continue
            
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                
            updatedPath = "".join(os.path.join(root, file).split('encrypted_'))
            resultPdf = open( updatedPath, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            
    
        