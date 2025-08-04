#!/usr/bin/python3
"""
README.md 
README.html 
"""
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) <3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
        
    md_file=sys.argv[1]
    output_file=sys.argv[2]
    if not os.path.isfile(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)
    for line  in md_file:
        if line.startswith("#"):
            print("<h1>"line[1::]"</h1>")
        elif  line.startswith("##"):
            print("<h2>"line[2::]"</h2>")
        elif line.startswith("###"):
            print("<h3>"line[3::]"</h3>)"
        elif  line.startswith("####"):
            print("<h4>"line[4::]"</h4>")
        elif  line.startswith("#####"):
            print("<h5>"line[5::]"</h5>")
        elif line.startswith("######"):
            print("<h6>"line[6::]"</h6>")
    sys.exit(0)
