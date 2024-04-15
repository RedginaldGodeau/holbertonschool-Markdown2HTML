"""
_main convert markdown to html :)
"""

from os.path import exists
import sys
if __name__ == "__main__":

    args = sys.argv
    if len(args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    inputFile = args[1]
    outputFile = args[2]

    if not exists(inputFile):
        sys.stderr.write("Missing " + inputFile)
        sys.exit(1)

    sys.exit(0)
