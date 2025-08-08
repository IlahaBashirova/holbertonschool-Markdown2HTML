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
        is_line = False
        ol_line = False

        for line in md:
            line = line.strip()
            count = 0
            for i in line:
                if i == "#":
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

            else:
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False
                if is_line:
                    html.write("</ul>\n")
                    is_line = False

            for x in range(len(line)):
                next_line_exists=x+1<len(line)
                next_line=line[x+1].strip() if next_line_exists else ""
            is_continuation= next_line !="" and not next_line.startswith("#") and not next_line.startswith("- ")
            if is_continuation:
                html.write("<p>"+line+"<br />")
            else:
                html.write(line+"</p>")
        if is_line:
            html.write("</ul>\n")
        if ol_line:
            html.write("</ol>\n")

    sys.exit(0)

