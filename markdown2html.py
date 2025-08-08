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
                for x in range(len(line)):
                    if line[x]=="*" and line[x+1]=="*":
                        html.write(f"<li>{line[2:x+1].strip()}<b> {line[x+2:x+4]}</b> {line[x+7::]}</li>\n")
                    else:
                        html.write(f"<li>{line[2:].strip()}</li>\n")

            elif line.startswith("* "):
                if not ol_line:
                    html.write("<ol>\n")
                    ol_line = True
                html.write(f"<li>{line[2:].strip()}</li>\n")
            
            #<p> text
            elif line != "":
                if is_line:
                    html.write("</ul>\n")
                    is_line = False
                if ol_line:
                    html.write("</ol>\n")
                    ol_line = False

                if i == 0 or lines[i - 1].strip() == "":
                    html.write("<p>\n")
                for c in range(len(line)):
                    if line[c]=="*" and line[c+1]=="*":
                        html.write(f"{line[0:c+1].strip()}<b> {line[c+2:c+4]}</b> {line[c+7::]}\n")

                if i + 1 < len(lines) and lines[i + 1].strip() != "" and not lines[i + 1].startswith(("#", "-", "*")):
                    html.write("<br/>\n")
                else:
                    html.write("</p>\n")
            #<b> <em>

                        
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

