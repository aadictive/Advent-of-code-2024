from constants import *
from utility.checkSort import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/2
def solution(identifier):
    puzzle_input = parse_file("day2.txt", identifier)
    # Write Solution here

    safe_reports_count = 0
    for inp in puzzle_input:
        stripped_inp = inp.strip()
        str_list = stripped_inp.split(" ")
        int_list = [int(x) for x in str_list]
        if are_reports_safe(int_list):
            safe_reports_count += 1

    return safe_reports_count


def are_reports_safe(reports):
    if check_int_if_sorted_asc_no_dup(reports) or check_int_if_sorted_desc_no_dup(reports):
        for i in range(len(reports) - 1):
            if abs(reports[i] - reports[i + 1]) > 3:
                return False
    else:
        return False

    return True


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
