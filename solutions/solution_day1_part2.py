from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/1
def solution(identifier):
    puzzle_input = parse_file("day1.txt", identifier)
    # Write Solution here
    left_list, right_list = [], []
    for inp in puzzle_input:
        strip_new_lines = inp.strip()
        llist, rlist = strip_new_lines.split("   ")
        left_list.append(int(llist))
        right_list.append(int(rlist))

    similarity_score = 0
    for left, right in zip(left_list, right_list):
        similarity_score += left * right_list.count(left)

    return similarity_score


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
