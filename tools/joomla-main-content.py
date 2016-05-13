#!/usr/bin/env python3
#Not yet usable!
#
# Converts a Joomla HTML page with standard templates into markdown syntax.
# Only main content in converted and everything else removed.
#
# This script might be used for other HTML page conversion
#

import getopt
import os
import re
import sys

opts, args = getopt.getopt(sys.argv[1:], "nd:v")

isReadOnly = False
isVerbose = False
rootDirectory = ""

for opt, arg in opts:
    if opt == "-d":
        rootDirectory = arg
    if opt == "-n":
        isReadOnly = True
    if opt == "-v":
        isVerbose = True

filePattern = ".*.html"
searchPatternSwitches = re.MULTILINE

if not rootDirectory:
    raise ValueError("No directory to search for HTML files given.")

print("Converting", rootDirectory, "for files like ", filePattern )

for subdir, dirs, files in os.walk(rootDirectory):
    for file in files:
        path = os.path.join(subdir, file)
        if (re.match(r'^'+filePattern+'$', file)):
            print("Convert file :", path)
            input = open(path,'r') 
            content = input.read()
            content = re.sub(r'(?<=<body id="page_bg" class="color_blue bg_blue width_fmax">).*(?=<table class="contentpaneopen">)', r'', content, 1, searchPatternSwitches)
            if not isReadOnly:
                outputFile = os.path.join(subdir, "converted-" + file)
                output = open(outputFile, 'w')
                output.write(content)
        else:
            if isVerbose:
                print("No matching files found in ", path)

