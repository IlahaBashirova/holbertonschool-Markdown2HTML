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
    with open (md_file, "r") as md, open (output_file, "w") as html:
        for line in md:
            line=line.strip()
            count=0
            for i in line:
                if i=="#":
                    count+=1
                else:
                    break
            if 1<=count<=6 and line[count:count+1]=" ":
                content=line[count::]
                html.write(f" <h{count}> {content} </h{count}>")
    sys.exit(0)
