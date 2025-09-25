import os, sys, subprocess
import re
from keywords import *
    
##===--------------------------------===##
def ParseFile():
    lines = []
    with open("CX/CXMAKE", "r") as file:
        for line in file:
            if any(ch.isalnum() for ch in line) == False:
                continue
            ln = line.strip()
            
            ln = line.split("//", 1)
        
            lines.append(ln[0])
    return lines

##===--------------------------------===##
def main():
    lines = ParseFile()

    for i in lines:
        syb = Symbol.ResolveSymbol(i) 
        if syb: print(syb.value)

    
        

##===--------------------------------===##
if __name__ == "__main__":
    main()