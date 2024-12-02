from constants import *
from utility.checkSort import *
from utility.parseFile import *

# Problem Statement: https://adventofcode.com/2024/day/2
def solution(identifier):
    input = parse_file("day2.txt", identifier)
    # Write Solution here

    safe_reports_count = 0
    for inp in input:
        stripped_inp = inp.strip()
        str_list = stripped_inp.split(" ")
        int_list = [int(x) for x in str_list]
        if are_reports_safe(int_list):
            safe_reports_count += 1
        elif is_safe_after_problem_dampner(int_list):
            safe_reports_count += 1

    return safe_reports_count

def are_reports_safe(input):
    if check_int_if_sorted_asc_no_dup(input) or check_int_if_sorted_desc_no_dup(input):
        for i in range(len(input) - 1):
            if abs(input[i] - input[i+1]) > 3:
                return False
    else:
        return False
    return True

def is_safe_after_problem_dampner(input):
    for i in range(len(input)):
        temp = input[:i] + input[i + 1:]
        if are_reports_safe(temp):
            return True

def executeOnExampleFile():
    return solution(EXAMPLE_FILE_IDENTIFIER)

def executeOnPuzzleFile():
    return solution(PUZZLE_FILE_IDENTIFIER)