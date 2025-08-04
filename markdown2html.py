#!/usr/bin/python3
"""
README.md 
README.html 
"""
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) <3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
        sys.exit(1)
        
    md_file=sys.argv[1]
    output_file=sys.argv[2]
    if not os.path.isfile(md_file):
        sys.stderr.write(f"Missing {md_file} \n")
        sys.exit(1)
    sys.exit(0)
