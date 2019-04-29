""" Simple program to count non space symbols in the file
    Usage: python count_symbols.py <filename> <columns>
"""

import re
import sys

_AUTHOR_ = "Andrii Khaietskyi"
_STATUS_ = "Draft"
_COPYRIGHT_ = "Copyright 2019"

def load_file(filename):
    """load file and return array of lines"""
    try:
        text_file = open(filename, "r")
        lines = text_file.readlines()
        text_file.close()
        print len(lines), "lines loaded"
        return lines
    except IOError:
        print "Error: File '" + filename + "'' doesn't exist or access denied"

def count_symbols(lines):
    """looks through each line and calculate non-space symbols"""
    symbols = {}
    for line in lines:
        for j in line:
            if re.search(r"\S", j):   #ignore space symbols
                if j in symbols:
                    symbols[j] += 1
                else:
                    symbols[j] = 1
    return symbols

def fancy_out(sym_dict, cols):
    """output formated result"""
    if not sym_dict:
        print "File has no symbols"
    else:
        print "The file contains next symbols and their quantity:"
        lines = len(sym_dict)
        total = 0
        cur_col = 0
        for key in sorted(sym_dict.keys()):
            print "{:<9}".format(key + ":" + str(sym_dict[key])),
            total += sym_dict[key]
            cur_col += 1
            if cur_col % cols == 0:
                print
        print
        print "Number of different symbols:", lines
        print "Total number of symbols:", total

if len(sys.argv) >= 2:
    LINES = load_file(sys.argv[1])
else:
    print "Please specify filename:", sys.argv[0], "<filename>"

SYMBOLS_DICT = count_symbols(LINES)
COLUMNS = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
fancy_out(SYMBOLS_DICT, COLUMNS)
