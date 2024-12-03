from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/X
def solution(identifier):
    input = parse_file("dayX.txt", identifier)
    # Write Solution here

    return 0


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)