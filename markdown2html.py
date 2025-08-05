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
        li=[]
        in_li=False
        for line in md:
            line=line.strip()
            count=0
            for i in line:
                if i=="#":
                    count+=1
        if line.startswith("- "):
            html.write("<ul>\n")
            in_li=True
            if in_li==True:
                html.write(line[2::])
            if in_li==False:
                html.write("<ul>\n")

            if 1<=count<=6 and line[count:count+1]==" ":
                content=line[count::]
                html.write(f" <h{count}> {content} </h{count}>\n")
    
    sys.exit(0)
