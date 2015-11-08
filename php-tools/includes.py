#!/usr/bin/env python3
#
# Search or remove include or require calls for a certain PHP file.
#

import getopt
import os
import re
import sys

opts, args = getopt.getopt(sys.argv[1:], "d:f:e:r:v:")

php_directory = "."
php_file = ""
php_file_extension_pattern = '(php)'
isDeletion = False
isVerbose = False

for opt, arg in opts:
    if opt == "-d":
        php_directory = arg
    if opt == "-f":
        php_file = arg
    if opt == "-r":
        isDeletion = True
    if opt == "-v":
        isVerbose = True
    if opt == "-e":
        php_file_extension_pattern = arg

if not php_file:
    raise ValueError("No PHP include file given to search for by -f option")

includePattern = r'(require_once|include_once|require|include)(\s*[(]?\s*[\'"][^\'"]*' + php_file + '[\'"]\s*[)]?\s*[;])'
includePatternPattern = re.IGNORECASE|re.MULTILINE

print("Converting", php_directory, "for PHP include", php_file)

for subdir, dirs, files in os.walk(php_directory):
    for file in files:
        path = os.path.join(subdir, file)
        if (re.match(r'.*\.'+php_file_extension_pattern+'$', file)):
            input = open(path,'r') 
            code = input.read()
            found = re.findall(includePattern, code, includePatternPattern)
            if found:
                for match in found:
                    print("PHP file with include for", php_file, ":", path, "with match:", ''.join(match))
                if isDeletion:
                    print("PHP file with removed include for", php_file, ":", path)
                    code = re.sub(includePattern, r'', code, 0, includePatternPattern)
                    output = open(path, 'w')
                    output.write(code)
        else:
            if isVerbose:
                print("No PHP file: ", path)

