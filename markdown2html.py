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

    input_file = args[1]
    output_file = args[2]

    if not exists(input_file):
        sys.stderr.write("Missing " + input_file + "\n")
        sys.exit(1)

    mardown_index = []
    current_array = []
    current_markdown_char = ""

    markdown = open(input_file, "r")
    for line in markdown:
        markdown_char = ""

        if "#" in line:
            markdown_char = "#"
            mardown_index.append({"char": "#", "line": line.replace("\n", "")})
        elif "-" in line:
            markdown_char = "-"
        elif "*" in line:
            markdown_char = "*"
        elif len(line) > 1:
            markdown_char = "txt"
        else:
            markdown_char = "other"

        if current_markdown_char == markdown_char and current_markdown_char != "#":
            current_array.append(
                {"char": markdown_char, "line": line.replace("\n", "")}
            )
        elif current_markdown_char != markdown_char and current_markdown_char != "#":
            mardown_index.append(current_array)
            current_array = []
            current_array.append(
                {"char": markdown_char, "line": line.replace("\n", "")}
            )
        current_markdown_char = markdown_char

    output_string = ""

    for index in mardown_index:
        if isinstance(index, list) == True and len(index) > 0:
            if index[0]["char"] == "-" or index[0]["char"] == "*":
                if index[0]["char"] == "-":
                    output_string += "<ul>\n"
                elif index[0]["char"] == "*":
                    output_string += "<ol>\n"
                for mrd in index:
                    text = mrd["line"].replace("-", "").replace("*", "").strip()
                    if mrd["char"] == "-" or mrd["char"] == "*":
                        output_string += "<li>{0}</li>\n".format(text)
                if index[0]["char"] == "-":
                    output_string += "</ul>\n"
                elif index[0]["char"] == "*":
                    output_string += "</ol>\n"
            elif index[0]["char"] == "txt":
                output_string += "<p>\n"
                for idx in range(len(index)):
                    text = index[idx]["line"].strip()
                    output_string += "{0}\n".format(text)
                    if len(index)-1 > idx:
                        output_string += "<br/>\n"
                output_string += "</p>\n"

        elif isinstance(index, dict) == True:
            if index["char"] == "#":
                num_of_header = index["line"].count("#")
                text = index["line"].replace("#", "").strip()
                output_string += "<h{0}>{1}</h{0}>\n".format(num_of_header, text)
    
    html = open(output_file, 'w')
    html.write(output_string)
    html.close()
    markdown.close()

    sys.exit(0)
