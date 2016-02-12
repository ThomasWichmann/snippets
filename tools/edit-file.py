#!/usr/bin/env python3
#
# Edit files with some given Regex replacement expression
#

import getopt
import os
import re
import sys

opts, args = getopt.getopt(sys.argv[1:], "d:f:r:s:n:v:")

rootDirectory = "."
searchPattern = ""
replacePattern = ""
filePattern = '.*'
isReadOnly = False
isVerbose = False

for opt, arg in opts:
    if opt == "-d":
        rootDirectory = arg
    if opt == "-s":
        searchPattern = arg
    if opt == "-r":
        replacePattern = arg
    if opt == "-n":
        isReadOnly = True
    if opt == "-v":
        isVerbose = True
    if opt == "-f":
        filePattern = arg

searchPattern = r'' + searchPattern
replacePattern = r'' + replacePattern
searchPatternSwitches = re.MULTILINE

if not searchPattern:
    raise ValueError("No search pattern given by -s option")

print("Converting", rootDirectory, "for files like ", filePattern , " with search pattern " , searchPattern )

for subdir, dirs, files in os.walk(rootDirectory):
    for file in files:
        path = os.path.join(subdir, file)
        if (re.match(r'^'+filePattern+'$', file)):
            input = open(path,'r') 
            content = input.read()
            found = re.findall(searchPattern, content, searchPatternSwitches)
            if found:
                for match in found:
                    print("File found with search pattern for :", path, "with match:", ''.join(match))
                    if not isReadOnly:
                        content = re.sub(searchPattern, replacePattern, content, 0, searchPatternSwitches)
                        output = open(path, 'w')
                        output.write(content)
        else:
            if isVerbose:
                print("No matching files found in ", path)

