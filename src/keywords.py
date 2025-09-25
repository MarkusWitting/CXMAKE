import os
import re

SymbolTypes = [
    "lit",
    "dir"
]

class Dir:
    @staticmethod
    def RecurSearch():
        pass

    def ResolveDir(dir_: str):
        search_type = "single"
        if "/**" in dir_: search_type = "recur" # all subfolders # add logic for this later

        path = (dir_.split()[0]).split("/")
        print(f"Path: {path}")

        file_exts = dir_.split()[1].split()
        print(f"File_types: {', '.join(file_exts)}")

        print()

        dirs = []
        files = []

        if search_type == "single":
            for file in os.listdir(path):
                for ft in file_exts:
                    if file.endswith(ft):
                        print(file)

        



class Symbol:
    def __init__(self, symbol_, value_):
        self.symbol = symbol_
        self.value = value_

    def ResolveSymbol(line: str):
        match = re.match(r"[a-zA-Z]+=", line)
        if match:
            symbol = match.group().replace("=", "")

            value = line.split("= ")[1].strip()
    
            value = Dir.ResolveDir(value)