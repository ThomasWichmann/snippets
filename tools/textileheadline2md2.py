#!/usr/bin/env python3
#
# Only converts textile headlines markup "h1., h2., ..." into markdown header
#

import re
import sys
import os
import pathlib
import fileinput
import shutil

filename = sys.argv[1]

print("Converting ", filename, pathlib.Path(filename).suffix)

if not pathlib.Path(filename).suffix == ".textile":
    raise Exception("File ", filename, " has wrong extension. It is no textile file.")

outputFilename = re.sub(r'\.textile$', ".md", filename)
shutil.copyfile(filename, outputFilename)

def headerRepl(matchobj):
    return ''.rjust(int(matchobj.group(1)),'#')

# Do some extra custom and aggressive cleanup
for line in fileinput.input(outputFilename, inplace=True):
    line = re.sub(r'h([1-5])\.', headerRepl, line)
    sys.stdout.write(line)
