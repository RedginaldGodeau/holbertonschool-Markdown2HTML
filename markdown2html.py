#!/usr/bin/python3

"""
_main convert markdown to html :)
"""

from os.path import exists
import sys

def clean_text(text, character):
    """clean_text

    Args:
        text (string): line to clean
        character (string): char clean

    Returns:
        string: result
    """
    return text.replace(character, "").replace("\n", "").strip()

def read_markdown_file (markdown_file):
    """read_markdown_file

    Args:
        markdownFile (string): file used for markdown to html

    Returns:
        string: the result of markdown to html
    """
    markdown = open(markdown_file, "r")
    output_str = ""
    current_u_list = False
    current_o_list = False

    for line in markdown:
        if "-" not in line and current_u_list:
            current_u_list = False
            output_str += "</ul>\n"
        if "*" not in line and current_o_list:
            current_o_list = False
            output_str += "</ol>\n"

        if "#" in line:
            headline_num = line.count("#")
            just_text = clean_text(line, "#")
            output_str += "<h{0}>{1}</h{0}>\n".format(headline_num, just_text)
        elif '-' in line:
            if not current_u_list:
                current_u_list = True
                output_str += "<ul>\n"
            just_text = clean_text(line, "-")
            output_str += "<li>{0}</li>\n".format(just_text)
        elif '*' in line:
            if not current_o_list:
                current_o_list = True
                output_str += "<ol>\n"
            just_text = clean_text(line, "*")
            output_str += "<li>{0}</li>\n".format(just_text)
    if current_u_list:
        output_str += "</ul>\n"
    if current_o_list:
        output_str += "</ol>\n"

    markdown.close()
    return output_str



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

    result = read_markdown_file(input_file)
    html = open(output_file, 'w')
    html.write(result)

    #print(OutputStr, end='')
    sys.exit(0)
