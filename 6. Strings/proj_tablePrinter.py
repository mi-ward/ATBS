tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    
def printTable(table):
    col_num = max(map(len, table))
    colWidth = [0] * len(table)
    
    for row in range(col_num):
        rowString = ''
        for col in range(len(table)):
            colWidth[col] = max(map(len, table[col]))
            rowString += table[col][row].rjust(colWidth[col]) + ' '
        print(rowString)
        
printTable(tableData)