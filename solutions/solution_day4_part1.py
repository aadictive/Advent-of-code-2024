from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/4
def solution(identifier):
    puzzle_input = read_file("day4.txt", identifier)
    # Write Solution here
    xmas = "XMAS"
    xmas_count = 0
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[row])):
            height = len(puzzle_input)
            width = len(puzzle_input[0])
            checks = []

            # only check part 1 if the current cell is X or S
            if puzzle_input[row][col] in ['X', 'S']:
                # horizontal check
                if col + 3 < width:
                    checks.append(puzzle_input[row][col:col + 4])

                # vertical check
                if row + 3 < height:
                    checks.append(str.join('', [puzzle_input[row + i][col] for i in range(0, 4)]))

                # diagonal check
                # top left to bottom right
                if row + 3 < height and col + 3 < width:
                    checks.append(str.join('', [puzzle_input[row + i][col + i] for i in range(0, 4)]))

                # top right to bottom left
                if row + 3 < height and col - 3 >= 0:
                    checks.append(str.join('', [puzzle_input[row + i][col - i] for i in range(0, 4)]))

                for check in checks:
                    xmas_count += int(string_check(check, xmas))

    return xmas_count


def string_check(to_check, check):
    return to_check == check or to_check == check[::-1]


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
