from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/1
def solution(identifier):
    input = parse_file("day1.txt", identifier)
    # Write Solution here
    left_list, right_list = [], []
    for inp in input:
        strip_new_lines = inp.strip()
        llist, rlist = strip_new_lines.split("   ")
        left_list.append(int(llist))
        right_list.append(int(rlist))

    similarity_score = 0
    for l, r in zip(left_list, right_list):
        similarity_score += l * right_list.count(l)

    return similarity_score


def executeOnExampleFile():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def executeOnPuzzleFile():
    return solution(PUZZLE_FILE_IDENTIFIER)