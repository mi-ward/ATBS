#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: pw.exe mcb.pyw save <keyword> - Saves clipboard to keyboard.
#        pw.exe mcb.pwy <keyword> - Loads keywords to clipboard.
#        pw.exe mcb.pwy list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in mcbShelf:
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    


mcbShelf.close()

