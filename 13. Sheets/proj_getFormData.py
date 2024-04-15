import ezsheets



ss = ezsheets.Spreadsheet('1KXYT1tDqSCl-v2kijedsd3Z7eYWUV_4uZ49RAxXax_o')
sheet = ss[0]
column_headers = sheet.getRow(1)

for idx, column_header in enumerate(column_headers, 1):
    if column_header.lower() == 'email address':
        email_column = sheet.getColumn(idx)

email_column = list(filter(bool, email_column))
print(email_column)
