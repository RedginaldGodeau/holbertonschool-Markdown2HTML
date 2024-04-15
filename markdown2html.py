#!/usr/bin/python3

"""
_main convert markdown to html :)
"""

from os.path import exists
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    inputFile = args[1]
    outputFile = args[2]

    if not exists(inputFile):
        sys.stderr.write("Missing " + inputFile + "\n")
        sys.exit(1)

    markdown = open(inputFile, "r")
    OutputStr = ""

    for line in markdown:
        if "#" in line:
            headerNum = line.count("#")
            justText = line.replace("#", "").replace("\n", "").strip()
            OutputStr += "<h{0}>{1}</h{0}>\n".format(headerNum, justText)

    html = open(outputFile, 'w')
    html.write(OutputStr)

    #print(OutputStr, end='')
    sys.exit(0)
