# Code written by TRC Loop - 2024
# For MCSLA
import sys
import os
EXPORT_FORMATS = ["excel-csv", "excel-sheet", "json", "txt", "rtf"]




def Questioning():
    path = str(input("Enter the path to the file or folder: "))
    format = str(input("Enter the export format: "))
    return path, format

def main(pathType: int, path: str, exportType: str):
    # Check if type is 0 or 1 else exit
    if pathType != 0 and pathType != 1:
        print("Path type not supported")
        sys.exit(1)
    
    # Check if export type is supported
    if exportType not in EXPORT_FORMATS:
        print("Export type not supported, valid types are: " + str(EXPORT_FORMATS))
        sys.exit(1)
    
    
    

if __name__ == "__main__":
    path = ""
    format = ""
    type = -1
    if len(sys.argv) >= 3:
        print("USAGE: python main.py <path> <format>")
        print("path: path to the file or folder, format: export format: excel-csv, excel-sheet, json, txt, rtf")
        print("Too many arguments")
        sys.exit(1)
        
    if len(sys.argv) == 0:
        path, format = Questioning()
    if len(sys.argv) == 2:
        path, format = sys.argv[1], sys.argv[2]
       

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
        sys.exit(1)
    
    main(type, path, format)