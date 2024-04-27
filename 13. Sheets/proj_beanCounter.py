import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet = ss[0]
column1 = sheet.getColumn(1)
column2 = sheet.getColumn(2)
column3 = sheet.getColumn(3)

for idx in range(1, len(column3)):
    total = int(column1[idx]) * int(column2[idx])
    if total != int(column3[idx]):
        print(column1[idx], column2[idx], column3[idx], total)
    
    


#14398