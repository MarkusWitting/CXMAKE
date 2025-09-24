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
def CheckFunc(func: fd.FUNC):
    for func_def in fd.FUNCDEFS:
        if func.name == func_def.name:
            for i in func.params:
                if i not in func_def.param_defs:
                    raise ValueError(f"Parameter {i} not valid for function {name}")
                else:
                    param_list.params.append(i)




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