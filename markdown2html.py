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
            while "**" in line:
                start = line.find("**")
                end = line.find("**", start + 2)
                if end == -1:
                    break
                line = line[:start] + "<b>" + line[start+2:end] + "</b>" + line[end+2:]
            while "__" in line:
                start = line.find("__")
                end=line.find("__",start+2)
                if end==-1:
                    break
                line=line[:start] + "<em>" + line[start+2:end] + "</em>" + line[end+2:]

            while "[[" in line and "]]" in line:
                start = line.find("[[")
                end = line.find("]]", start + 2)
                if end == -1:
                    break
                content = line[start+2:end].lower()
                md5_text = hashlib.md5(content.encode()).hexdigest()
                line = line[:start] + md5_text + line[end+2:]

            
            while "((" in line and "))" in line:
                start = line.find("((")
                end = line.find("))", start + 2)
                if end == -1:
                    break
                content = line[start+2:end].replace("c", "").replace("C", "")
                line = line[:start] + content + line[end+2:]

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
                html.write(f"{line}\n")
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

