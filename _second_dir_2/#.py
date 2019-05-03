_author_ = "Andrii Khaietskyi"
_status_ = "Draft"
_copyright_ = "Copyright 2019"

"""
Simple program to count non space symbols in the file
"""

import re
import sys

def load_file( filename ):
    try:
        text_file = open(filename, "r")
        lines = text_file.readlines()
        text_file.close()
        print len(lines), "lines loaded"
        return lines
    except IOError:
        print "Error: File '" + filename + "'' doesn't exist or access denied"

def count_symbols( lines ):
    symbols = {}
    for line in lines:
        for j in line:
            if re.search("\S",j):   #ignore space symbols
                if j in symbols:
                    symbols[j] += 1
                else:
                    symbols[j] = 1
    return symbols

def fancy_out( dict, columns ):
    if not dict:
        print "File has no symbols"
    else:
        print "The file contains next symbols and their quantity:"
        lines = len(dict)
        total = 0
        n = 0
        for key in sorted(dict.keys()):
            print "{:<9}".format(key + ":" + str(dict[key])),
            total += dict[key]
            n += 1
            if n % columns == 0:
                print
        print
        print "Number of different symbols:", lines
        print "Total number of symbols:", total

if len(sys.argv) >= 2:
    lines = load_file(sys.argv[1])
else:
    print "Please specify filename:", sys.argv[0], "<filename>"

symbols_dict = count_symbols(lines)
columns = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
fancy_out(symbols_dict, columns)
