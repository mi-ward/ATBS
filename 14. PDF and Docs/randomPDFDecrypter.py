import random
import PyPDF2

words = []
word_file = open('dictionary.txt', 'r')

for word in word_file:
    words.append(word.strip())

word_file.close()
    
num = random.randint(0, len(words))

pdf_to_decrypt = PyPDF2.PdfFileReader('./DECRYPTME.PDF')

for word in words:
    print(word)
    if pdf_to_decrypt.decrypt(word) == 1:
        print(word)
        break

                





