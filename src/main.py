import typer
from rich import print
from rich.prompt import Confirm
from Scripts.ILib import *
import os.path
app = typer.Typer()



@app.command()
def analyze(log_path: str, export_format: FileType, export_path: str, verbose: bool = False, no_ask: bool = False):
    LoadLog_spinner.start()
    logtxt: str = ""
    
    LoadLog_spinner.info("Checking Path") if verbose else None
    if not os.path.exists(log_path):
        LoadLog_spinner.fail("Path not Found: " + log_path)
        print("[bold red]Path not Found: [blue]" + log_path)
        raise typer.Exit(code=1)
    
    LoadLog_spinner.info("Checking if .log") if verbose else None
    if not log_path.endswith(".log"):
        LoadLog_spinner.warn("Not a .log file")
        if not Confirm.ask("File does not end with .log, are you sure this is a valid file? "):
            LoadLog_spinner.fail("Invalid File (UA)")
            print("[bold red]Invalid File (User Aborted)")
            raise typer.Exit(code=1)

    LoadLog_spinner.info("Loading Log (Read)") if verbose else None
    with open(log_path, "r") as file:
        logtxt = file.read()
    
    LoadLog_spinner.succeed("Log Loaded")

@app.command()
def toFormat(file_path: str, export_format: FileType, verbose: bool = False):
    print("Converting file: ", file_path, " to ", export_format)

if __name__ == "__main__":
    app()
