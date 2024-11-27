from constants import *
from utility.parseFile import *

# Problem Statement: https://adventofcode.com/2024/day/1
def solution(identifier):
    input = parse_file("day1_part1.txt", identifier)
    # Write Solution here

    return 0


def executeOnExampleFile():
    return solution(EXAMPLE_FILE_IDENTIFIER)

def executeOnPuzzleFile():
    return solution(PUZZLE_FILE_IDENTIFIER)