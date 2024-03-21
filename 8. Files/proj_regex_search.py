#! python3
# proj_regex_search.py - searches all files in a directory for a regex value and returns the file name and line if it contains it

import os, sys, re, pprint

ls = os.listdir(sys.argv[1])
reg_ex = re.compile(sys.argv[2])

matches_dict = {}

def filter_for_txt(file):
    return file.endswith('.txt')

files_to_scan = list(filter(filter_for_txt, ls))

enum = 0 
for file in files_to_scan:
    scan_file = open(file)
    lines = scan_file.readlines()
    for line in lines:
        result = reg_ex.search(line)
        if result is not None:
            enum += 1
            matches_dict.setdefault(enum, (file, result.group(0), line))
    scan_file.close()

pprint.pprint(matches_dict)




