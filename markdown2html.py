#!/usr/bin/env python3
import sys
import os
if len(sys.argv) < 2:
    sys.stder.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

md_file=sys.argv(1)

if not os.path.isfile(md_file):
    sys.stder.write(f"Missing {md_file} /n")
    sys.exit(1)
sys.exit(0)
