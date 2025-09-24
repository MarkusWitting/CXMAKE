import os, sys, subprocess
import re
import funcdef as fd
    
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
def GetFuncs(lines):
    for ln in lines:
        temp_funcs = []
        match = re.match(r'([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)', ln)
        if match:
            func_name = match.group(1)
            params = match.group(2).split(',')
            params = [param.strip().split() for param in params]

            temp_funcs.append(fd.FUNC(func_name, params))
    return temp_funcs

##===--------------------------------===##
# Add CheckFunc Function



##===--------------------------------===##
def GetProjectInfo(lines):
    for ln in lines:
        pass

##===--------------------------------===##
def main():
    lines = ParseFile()
    
    #funcs = GetFuncs(lines)
    print(CheckFunc(fd.FUNC("Project", ["MyApp", "1.0", "C++"])))

##===--------------------------------===##
if __name__ == "__main__":
    main()