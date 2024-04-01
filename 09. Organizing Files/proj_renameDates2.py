#! python3
# proj_renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

#create a regex that matches files with the American Date format.
datePattern = re.compile(r"""^(.*?)         # all text before the date
                         ((0|1|2|3)?\d)-    # one or two digits for the day
                         ((0|1)?\d)-        # one or two digits for the month
                         ((19|20)\d\d)      # four digits for the year
                         (.*?)$             # all text after the date
                         """, re.VERBOSE)

# Loop over the files in the working directory
for euroFileName in os.listdir('./renameDatesFile1'):
    mo = datePattern.search(euroFileName)

    #Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    dayPart    = mo.group(2)
    monthPart  = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


    # Form the European-style filename.
    amerFileName = beforePart + monthPart +'-'+ dayPart +'-'+ yearPart + afterPart
    
    # Get the full absolute, file paths.
    absWorkingDirectory = os.path.abspath('./renameDatesFile1')
    amerFileName = os.path.join(absWorkingDirectory, amerFileName)
    euroFileName = os.path.join(absWorkingDirectory, euroFileName)
    
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (euroFileName, amerFileName))
    shutil.move(euroFileName, amerFileName)        #uncomment after testing


