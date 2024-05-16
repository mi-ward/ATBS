import random
import PyPDF2

words = []
word_file = open('dictionary.txt', 'r')

for word in word_file:
    words.append(word.strip())

word_file.close()
    
num = random.randint(0, len(words))

pdf_to_encrypt = PyPDF2.PdfFileReader('./ENCRYPTME.PDF')
pdf_to_decrypt = PyPDF2.PdfFileWriter()

for pageNum in range(pdf_to_encrypt.numPages):
    pdf_to_decrypt.addPage(pdf_to_encrypt.getPage(pageNum))
                
pdf_to_decrypt.encrypt(words[num])
resultPdf = open('./DECRYPTME.pdf', 'wb')
pdf_to_decrypt.write(resultPdf)
resultPdf.close()





