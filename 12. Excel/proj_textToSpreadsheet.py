import os, openpyxl

dir = './textfiles'

files = sorted(list(filter(lambda f: f.endswith('txt'), 
                      list(map(lambda f: os.path.join(os.path.abspath(dir), os.path.basename(f)), 
                               os.listdir('./textfiles'))))))

wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = 'Text Files'

for row_idx in range(0, len(files)):
    fo = open(files[row_idx], 'r')
    line_list = fo.readlines()
    
    for col_idx in range(0, (len(line_list))):
        sheet.cell(row=(row_idx+1), column=(col_idx+1)).value = line_list[col_idx]
    fo.close()
    

wb.save('textfiles.xlsx')