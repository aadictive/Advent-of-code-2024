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
    with open(full_path, "r") as lines:
        puzzle_input = lines.readlines()
    return puzzle_input


def read_file(filename, identifier, split_lines=True):
    full_path = ""
    if identifier == EXAMPLE_FILE_IDENTIFIER:
        full_path = path.joinpath(exampleFilesPath, filename)
    elif identifier == PUZZLE_FILE_IDENTIFIER:
        full_path = path.joinpath(puzzleFilesPath, filename)
    with open(full_path, "r") as lines:
        puzzle_input = lines.read()
    return puzzle_input.splitlines() if split_lines else puzzle_input