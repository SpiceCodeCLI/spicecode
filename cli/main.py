import os
import sys
import typer

# import commands
from cli.commands.translate import translate_command
from cli.commands.hello import hello_command
from cli.commands.version import version_command
from cli.commands.analyze import analyze_command


# initialize typer
app = typer.Typer()

# add the current directory (cli) to the sys.path
sys.path.append('cli')

# get current directory, this is needed for it to work on other peoples computers via pip
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# select a file to save the current selected langague (if saved to memory it wont persist between commands)
LANG_FILE = os.path.join(CURRENT_DIR, "lang.txt")



# SPICE TRANSLATE COMMAND
@app.command()
def translate():
    """
    Set the language for CLI messages.
    """

    translate_command(LANG_FILE)

# -- end -- #


# SPICE HELLO COMMAND
@app.command()
def hello():
    """
    Welcome message.
    """

    hello_command(LANG_FILE)

# -- end -- #


# SPICE VERSION COMMAND
@app.command()
def version():
    """
    Display the current version of the application.
    """
    
    version_command(LANG_FILE, CURRENT_DIR)

#--- end ---#


# SPICE ANALYZE COMMAND
@app.command()
def analyze(
    file: str, 
    all: bool = typer.Option(False, "--all", help="Analyze all stats without selection menu"),
    json_output: bool = typer.Option(False, "--json", help="Output results in JSON format")
):
    """
    Analyze the given file.
    """
    
    analyze_command(file, all, json_output, LANG_FILE)

# -- end -- #


def main():
    app()  # run typer

# -- end -- #


# whatever the fuck this is python makes no sense
if __name__ == "__main__":
    main()

# -- end -- #