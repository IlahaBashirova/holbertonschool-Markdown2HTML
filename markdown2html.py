#!/usr/bin/python3
"""
This script checks a Markdown file and outputfile arguments.
"""
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stder.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

md_file=sys.argv(1)

    if not os.path.isfile(md_file):
        sys.stder.write(f"Missing {md_file} /n")
        sys.exit(1)
sys.exit(0)
