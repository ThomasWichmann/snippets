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

filePattern = "Links.html"
searchPatternSwitches = re.MULTILINE|re.DOTALL

if not rootDirectory:
    raise ValueError("No directory to search for HTML files given.")

print("Converting", rootDirectory, "for files like ", filePattern )

def replaceTdByClass(html, classAttribute):
    return re.sub(r'<td class="'+classAttribute+'"[^>]*>[^<]+</td>', r'', html, 1, searchPatternSwitches)

def replaceFileExtension(path, extension):
    if path.find('.') == -1:
        return path + extension
    else:
        return re.sub(r'.[^.]*$', extension, path)

for subdir, dirs, files in os.walk(rootDirectory):
    for file in files:
        path = os.path.join(subdir, file)
        if re.match(r'^'+filePattern+'$', file):
            print("Convert file :", path)
            input = open(path,'r') 
            content = input.read()
            content = re.sub(r'(?<=<body id="page_bg" class="color_blue bg_blue width_fmax">).*(?=<table class="contentpaneopen">)', r'', content, 1, searchPatternSwitches)
            content = re.sub(r'Written by [^<]+', r'', content, 1)
            content = replaceTdByClass(content, 'createdate')
            content = replaceTdByClass(content, 'modifydate')
            content = re.sub(r'(?<=<div id="footer">).*(?=</body>)', r'', content, 1, searchPatternSwitches)

            outputFilename = "converted-" + file
            outputPath = os.path.join(subdir, outputFilename)
            mdPath = replaceFileExtension(outputPath, '.md')
            pandocSystemCall = 'pandoc -s --metadata="generator:Wichmann joomla-content-to-markdown converter" -o ' + mdPath + ' ' + outputPath
            print('Pandoc call: ', pandocSystemCall)
            
            if not isReadOnly:
                output = open(outputPath, 'w')
                output.write(content)
                os.system(pandocSystemCall)
                mdInput = open(mdPath,'r') 
                mdContent = mdInput.read()                
                mdContent = mdContent.replace('\\','');
                mdOutput = open(mdPath, 'w')
                mdOutput.write(mdContent)

        else:
            if isVerbose:
                print("No matching files found in ", path)

