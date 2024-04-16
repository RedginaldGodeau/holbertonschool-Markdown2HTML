#!/usr/bin/python3

"""
_main convert markdown to html :)
"""

from os.path import exists
import sys
import re

def text_transform(txt):
    """text_transform

    Args:
        txt (string): text to transform

    Returns:
        string: transformed 
    """
    formatted_text = re.sub(r"__([^_]+)__(?!_)", r"<em>\1</em>", txt)
    formatted_text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", formatted_text)
    return formatted_text

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

    markdown = open(input_file, "r")
    mardown_index = []
    for line in markdown:
        if line.startswith("#"):
            mardown_index.append({"char": "#", "line": line.replace("\n", "")})
        elif line.startswith("-"):
            mardown_index.append({"char": "-", "line": line.replace("\n", "")})
        elif line.startswith("*") and not line.startswith("**"):
            mardown_index.append({"char": "*", "line": line.replace("\n", "")})
        elif len(line) > 1:
            mardown_index.append({"char": "txt", "line": line.replace("\n", "")})
        else:
            mardown_index.append({"char": "other", "line": line.replace("\n", "")})

    markdown_grouped = []
    current_group = []
    prev_item = None
    for index in mardown_index:
        if prev_item is None:
            prev_item = index
            current_group.append(prev_item)
            continue

        if prev_item["char"] == index["char"]:
            if len(current_group) == 0:
                current_group.append(prev_item)
            current_group.append(index)
        elif prev_item["char"] != index["char"]:
            if len(current_group) >= 1:
                markdown_grouped.append(current_group)
            current_group = []
            current_group.append(index)

        prev_item = index

    output_str = ""
    for index in markdown_grouped:
        if isinstance(index, list):
            if index[0]["char"] == "#":
                for mrdtohtml in index:
                    text = mrdtohtml["line"].replace("#", "").strip()
                    output_str += "<h{0}>{1}</h{0}>\n".format(mrdtohtml["line"].count("#"), text_transform(text))
            elif index[0]["char"] == "-":
                output_str += "<ul>\n"
                for mrdtohtml in index:
                    text = mrdtohtml["line"][1:].strip()
                    output_str += "<li>{0}</li>\n".format(text_transform(text))
                output_str += "</ul>\n"
            elif index[0]["char"] == "*":
                output_str += "<ol>\n"
                for mrdtohtml in index:
                    text = mrdtohtml["line"][1:].strip()
                    output_str += "<li>{0}</li>\n".format(text_transform(text))
                output_str += "</ol>\n"
            elif index[0]["char"] == "txt":
                output_str += "<p>\n"
                for i, mrdtohtml in enumerate(index):
                    text = mrdtohtml["line"].strip()
                    output_str += text_transform(text) + "\n"
                    if i != len(index) - 1:
                        output_str +=  "<br/>\n"
                output_str += "</p>\n"
    html = open(output_file, 'w')
    html.write(output_str)
    html.close()
    markdown.close()
    sys.exit(0)
