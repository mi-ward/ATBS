import pyperclip

text = pyperclip.paste()

line_arr = text.split('\n')
string_to_copy = ''

for i in line_arr:
   if i != '':
       string_to_copy += '* ' + i + '\n'

pyperclip.copy(string_to_copy)

###Book Solution
# Separate lines and add stars
# lines = text.split('\n')
# for i in range(len(lines)):     # loop through all indexes for "lines" list
#     lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
# text = '\n'.join(lines)
#pyperclip.copy(text)