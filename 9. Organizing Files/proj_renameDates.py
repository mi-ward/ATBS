#! python3
# proj_renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

#create a regex that matches files with the American Date format.
datePattern = re.compile(r"""^(.*?)         # all text before the date
                         ((0|1)?\d)-        # one or two digits for the month
                         ((0|1|2|3)?\d)-    # one or two digits for the day
                         ((19|20)\d\d)      # four digits for the year
                         (.*?)$             # all text after the date
                         """, re.VERBOSE)

# Loop over the files in the working directory
for amerFileName in os.listdir('./renameDatesFile1'):
    mo = datePattern.search(amerFileName)

    #Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


    # Form the European-style filename.
    euroFileName = beforePart + dayPart +'-'+ monthPart +'-'+ yearPart + afterPart
    
    # Get the full absolute, file paths.
    absWorkingDirectory = os.path.abspath('./renameDatesFile1')
    amerFileName = os.path.join(absWorkingDirectory, amerFileName)
    euroFileName = os.path.join(absWorkingDirectory, euroFileName)
    
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFileName, euroFileName))
    shutil.move(amerFileName, euroFileName)        #uncomment after testing


