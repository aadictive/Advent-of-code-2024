from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/4
def solution(identifier):
    puzzle_input = read_file("day4.txt", identifier)
    # Write Solution here
    mas = "MAS"
    mas_count = 0
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[row])):
            height = len(puzzle_input)
            width = len(puzzle_input[0])

            if puzzle_input[row][col] in ['M', 'S']:
                # mas in form of X count
                if row + 2 < height and col + 2 < width:
                    # top left to bottom right
                    right = str.join('', [puzzle_input[row + i][col + i] for i in range(0, 3)])
                    right_check = string_check(right, mas)

                    # top right to bottom left
                    left = str.join('', [puzzle_input[row + i][col + 2 - i] for i in range(0, 3)])
                    left_check = string_check(left, mas)

                    if right_check and left_check:
                        mas_count += 1

    return mas_count


def string_check(to_check, check):
    return to_check == check or to_check == check[::-1]


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
