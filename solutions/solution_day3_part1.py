from constants import *
from utility.parseFile import *
import re


# Problem Statement: https://adventofcode.com/2024/day/3
def solution(identifier):
    input = parse_file("day3.txt", identifier)

    # Write Solution here
    sum = 0
    pattern = r"mul\([\d]{1,3},[\d]{1,3}\)|don't\(\)|do\(\)"
    for inp in input:
        matches = re.findall(pattern, inp)
        for match in matches:
            if match.startswith("mul"):
                product = multiply_instruction(match)
                sum += product

    return sum


def multiply_instruction(mul):
    numbers = mul.replace("mul(", "").replace(")", "").split(",")
    return int(numbers[0]) * int(numbers[1])


def executeOnExampleFile():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def executeOnPuzzleFile():
    return solution(PUZZLE_FILE_IDENTIFIER)
