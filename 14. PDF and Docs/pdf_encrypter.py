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
        print(file)
        if file.endswith('.pdf'):
            print(file)
            oldPath = os.path.join(root, file)
            pdfFile = open(oldPath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                
            pdfWriter.encrypt(pw)
            updatedPath = os.path.join(root, ('encrypted_' + file))
            resultPdf = open(updatedPath, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            
            encryptedPDFReader = PyPDF2.PdfFileReader(open(updatedPath, 'rb'))
            if encryptedPDFReader.decrypt(pw) == True:
                print('file encrypted correctly')
                print('deleting original')
                send2trash(oldPath)
                #delete orignal code
            
    
        
    
    


