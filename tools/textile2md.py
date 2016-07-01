#!/usr/bin/env python3
#
# Edit files with some given Regex replacement expression
#

import re
import sys
import os
import pathlib
import fileinput

filename = sys.argv[1]

print("Converting ", filename, pathlib.Path(filename).suffix)

if not pathlib.Path(filename).suffix == ".textile":
    raise Exception("File ", filename, " has wrong extension. It is no textile file.")

outputFilename = re.sub(r'\.textile$', ".md", filename)
os.system("pandoc --no-wrap -o " + outputFilename + " " + filename)    

# Do some extra custom and aggressive cleanup
for line in fileinput.input(outputFilename, inplace=True):
    line = re.sub(r'\\$', "", line)
    line = re.sub(r'\\[_:#>$]', "", line)
    line = re.sub(r'~~', "-", line)
    line = re.sub(r'\\\*', "*", line)
    line = re.sub(r'h2\.', "##", line)
    line = re.sub(r'h3\.', "###", line)
    line = re.sub(r'h4\.', "####", line)
    sys.stdout.write(line)
