#! python3

#proj_blankLineInserter.py - inserts blank lines at specified point

import sys, openpyxl

file = sys.argv[1]
start = int(sys.argv[2])
blank_line_num = int(sys.argv[3])

wb = openpyxl.load_workbook(file)
ws = wb.active

ws.insert_rows(start, blank_line_num)

wb.save(file)


