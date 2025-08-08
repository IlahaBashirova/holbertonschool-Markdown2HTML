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
        lines=md.readlines()
        is_line = False
        ol_line = False

        for i in range(len(lines)):
            line = lines[i].strip()
            count = 0
            for ch in line:
                if ch == "#":
                    count += 1
                else:
                    break

            if 1 <= count <= 6 and line[count:count + 1] == " ":
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                content = line[count:].strip()
                html.write(f"<h{count}>{content}</h{count}>\n")

            elif line.startswith("- "):
                if not is_line:
                    html.write("<ul>\n")
                    is_line = True
                html.write(f"<li>{line[2:].strip()}</li>\n")

            elif line.startswith("* "):
                if not ol_line:
                    html.write("<ol>\n")
                    ol_line = True
                html.write(f"<li>{line[2:].strip()}</li>\n")

            elif line !="":
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                next_line_exists= i+1 < len(lines)  
                if next_line_exists:
                    next_line= lines[i+1].strip() 
                    is_continuation= next_line !="" and not next_line.startswith("#") and not next_line.startswith("* ") and not next_line.startswith("- ")
                else:
                    is_continuation = False
                if is_continuation:
                    html.write(f"<p>\n{line}\n<br />\n")
                else:
                    html.write(f"<p>\n{line}\n</p>\n")
            
            else:
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
        if is_line:
            html.write("</ul>\n")
        if ol_line:
            html.write("</ol>\n")

    sys.exit(0)

