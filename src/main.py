# Code written by TRC Loop - 2024
# For MCSLA
import sys
import os


def Questioning():
    ...

def main(type: int, path: str, format: str):
    print("Hello World!")
    
    
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if len(sys.argv) > 2:
            print("Too many arguments")
            print("USAGE: python main.py <path> <format>")
            print("path: path to the file or folder, format: export format: excel-csv, escel-sheet, json, txt, rtf")
        # Check if input is valid
        path = sys.argv[1]
        format = sys.argv[2]
        
        # Check if path is a folder or a file and if it exists
        if os.path.exists(path):
            if os.path.isdir(path):
                type = 1
            else:
                type = 0
        else:
            print("Path does not exist")
            print("USAGE: python main.py <path> <format>")
            print("path: path to the file or folder, format: export format: excel-csv, excel-sheet, json, txt, rtf")