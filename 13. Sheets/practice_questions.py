#Practice Questions

# 1. What three files do you need for EZSheets to access Google Sheets?
    # credentials file, token for drive, token for sheets

#2. What two types of objects does EZSheets have?
    # sheets (worksheets) and spreadsheets

#3. How can you create an Excel file from a Google Sheet spreadsheet?
    # use the ezsheets.downloadAsExcel()

#4. How can you create a Google Sheet spreadsheet from an Excel file?
    # use the ezsheets.upload() function

#5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?
    # ss['Students']['B2']

#6. How can you find the column letters for column 999?
    # ss.getLetterForColumn(999)

#7. How can you find out how many rows and columns a sheet has?
    # ss.rowCount and ss.columnCount

#8. How do you delete a spreadsheet? Is this deletion permanent?
    #ss.delete(), only if you add the flag, (permanent=True)

#9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
    # ezsheets.createSpreadsheet('title')
    # ezsheets.createSheet('title')

#10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
    # Calls will be slower