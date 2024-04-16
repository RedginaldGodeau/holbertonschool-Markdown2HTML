# Markdown to HTML Converter

This is a simple Python script that converts Markdown files to HTML. It parses various Markdown syntax elements and generates corresponding HTML markup.

## Usage

To use this script, follow these steps:

1. Make sure you have Python 3.7 or higher installed on your system.
2. Clone or download this repository.
3. Navigate to the directory containing the script.
4. Run the script with the following command:

```bash
./markdown2html.py <input_file.md> <output_file.html>
```
Replace <input_file.md> with the name of your Markdown file and <output_file.html> with the desired name for the output HTML file.

## Requirements
- Python 3.7 or higher
- Ubuntu 18.04 LTS

## Functionality
The script parses the following Markdown syntax elements:

- Headings
- Unordered and Ordered lists
- Paragraphs
- Bold text (```__text__``` and ```**text**```)

## Error Handling
The script includes error handling for the following scenarios:

- Insufficient number of arguments provided: prints Usage: ./markdown2html.py <input_file.md> <output_file.html> to STDERR and exits with code 1.
- Missing Markdown file: prints Missing <filename> to STDERR and exits with code 1.
- Otherwise, no output is printed, and the script exits with code 0.

## Example
Suppose you have a Markdown file named README.md and you want to convert it to HTML and save it as output.html. You would run the following command:

```bash
./markdown2html.py README.md output.html
This would generate the HTML output and save it to output.html.
```

```css
Feel free to adjust the content or formatting as needed!
```