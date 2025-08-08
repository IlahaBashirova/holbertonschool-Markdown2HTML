#!/usr/bin/python3
"""
markdown2html.py - A script that converts a Markdown (.md) file to an HTML (.html) file.

Supported Markdown elements:
- Headers (#, ##, ..., ######)
- Unordered lists (lines starting with -)
- Ordered lists (lines starting with *)

Usage:
    ./markdown2html.py README.md README.html
"""
import sys
import os
import hashlib

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    with open(md_file, "r") as md, open(output_file, "w") as html:
        lines = md.readlines()
        is_line = False
        ol_line = False

        for i in range(len(lines)):
            line = lines[i].strip()
            
            # Process special syntax first, before other formatting
            # Handle [[ ]] syntax - convert to MD5 hash
            while "[[" in line and "]]" in line:
                start = line.find("[[")
                end = line.find("]]", start + 2)
                if end == -1:
                    break
                content = line[start+2:end]  # Don't convert to lowercase
                md5_text = hashlib.md5(content.encode()).hexdigest()
                line = line[:start] + md5_text + line[end+2:]

            # Handle (( )) syntax - remove all 'c' and 'C' characters
            while "((" in line and "))" in line:
                start = line.find("((")
                end = line.find("))", start + 2)
                if end == -1:
                    break
                content = line[start+2:end].replace("c", "").replace("C", "")
                line = line[:start] + content + line[end+2:]

            # Handle bold syntax **text** -> <b>text</b>
            while "**" in line:
                start = line.find("**")
                end = line.find("**", start + 2)
                if end == -1:
                    break
                line = line[:start] + "<b>" + line[start+2:end] + "</b>" + line[end+2:]
            
            # Handle emphasis syntax __text__ -> <em>text</em>
            while "__" in line:
                start = line.find("__")
                end = line.find("__", start + 2)
                if end == -1:
                    break
                line = line[:start] + "<em>" + line[start+2:end] + "</em>" + line[end+2:]

            # Count header level
            count = 0
            for ch in line:
                if ch == "#":
                    count += 1
                else:
                    break

            # Handle headers
            if 1 <= count <= 6 and len(line) > count and line[count] == " ":
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                content = line[count+1:].strip()
                html.write(f"<h{count}>{content}</h{count}>\n")

            # Handle unordered list items
            elif line.startswith("- "):
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                if not is_line:
                    html.write("<ul>\n")
                    is_line = True
                html.write(f"<li>{line[2:].strip()}</li>\n")

            # Handle ordered list items
            elif line.startswith("* "):
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if not ol_line:
                    html.write("<ol>\n")
                    ol_line = True
                html.write(f"<li>{line[2:].strip()}</li>\n")
            
            # Handle paragraph text
            elif line != "":
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False

                if i == 0 or lines[i - 1].strip() == "":
                    html.write("<p>\n")
                html.write(f"{line}\n")
                if i + 1 < len(lines) and lines[i + 1].strip() != "" and not lines[i + 1].startswith(("#", "-", "*")):
                    html.write("<br/>\n")
                else:
                    html.write("</p>\n")
            
            # Handle empty lines
            else:
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                if is_line:
                    html.write("</ul>\n")
                    is_line = False

        # Close any remaining open lists
        if is_line:
            html.write("</ul>\n")
        if ol_line:
            html.write("</ol>\n")

    sys.exit(0)
