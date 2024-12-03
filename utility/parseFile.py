from pathlib import Path
from constants import *

path = Path.cwd().joinpath("codeInputs")
exampleFilesPath = "exampleFiles/"
puzzleFilesPath = "puzzleFiles/"


def parse_file(filename, identifier):
    full_path = ""
    if identifier == EXAMPLE_FILE_IDENTIFIER:
        full_path = path.joinpath(exampleFilesPath, filename)
    elif identifier == PUZZLE_FILE_IDENTIFIER:
        full_path = path.joinpath(puzzleFilesPath, filename)
    lines = open(full_path, "r")
    puzzle_input = lines.readlines()
    return puzzle_input
