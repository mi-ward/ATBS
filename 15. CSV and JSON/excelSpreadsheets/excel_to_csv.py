#python3!

import os, openpyxl, csv


for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if excelFile.endswith('.xlsx'):
        wb = openpyxl.load_workbook(excelFile)
        fileName = os.path.splitext(excelFile)[0]
    else:
        continue

    # Loop through every sheet in the workbook.
    for sheet in wb:
        # Create the CSV filename from the Excel filename and sheet title.
        csvFileName = fileName + '_' + sheet.title + '.csv'
        outputFile = open(csvFileName, 'w')
        # Create the csv.writer object for this CSV file.
        csvFile = csv.writer(outputFile)
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []   # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)

            # Write the rowData list to the CSV file.
            csvFile.writerow(rowData)

        outputFile.close()