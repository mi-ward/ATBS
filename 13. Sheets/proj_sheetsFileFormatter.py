import sys, ezsheets

ss = ezsheets.upload(sys.argv[1])
file_type = sys.argv[2]
if file_type.lower() == 'csv':
    ss.downloadAsCSV()
elif file_type.lower() == 'html':
    ss.downloadAsHTML()
elif file_type.lower() == 'ods':
    ss.downloadAsODS()
elif file_type.lower() == 'pdf':
    ss.downloadAsPDF()
elif file_type.lower() == 'tsv':
    ss.downloadAsTSV()
elif file_type.lower() == 'xlsx':
    ss.downloadAsExcel()
else:
    print('Not a valid file type.')
    


