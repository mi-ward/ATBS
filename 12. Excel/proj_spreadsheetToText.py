import os, openpyxl

directory = 'new_textfiles'

os.makedirs('./'+directory, exist_ok=True)
dirpath = os.path.abspath(directory)

wb = openpyxl.load_workbook('./textfiles.xlsx')
ws = wb.active

row_max = ws.max_row
col_max = ws.max_column

for x in range(1, row_max+1):
    fo = open(os.path.join(dirpath, (str(x) + '.txt')), 'w')
    for y in range(1, col_max+1):
        try:
            fo.write(ws.cell(row=x, column=y).value)
        except:
            continue
    fo.close()