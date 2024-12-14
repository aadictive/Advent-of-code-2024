import constants
from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/14
def solution(identifier):
    puzzle_input = read_file("day14.txt", identifier)
    # Write Solution here
    robots = []
    for line in puzzle_input:
        a, b = line.split(" ")
        x, y = map(int, a[2:].split(","))
        vx, vy = map(int, b[2:].split(","))
        robots.append(((x, y), (vx, vy)))

    width = 101
    height = 103

    # for the test input
    if len(robots) == 12:
        width = 11
        height = 7

    quads = [0, 0, 0, 0]

    # there’s no need to loop 100 times
    for i in range(len(robots)):
        (x, y), (vx, vy) = robots[i]
        x = (x + 100 * (vx + width)) % width
        y = (y + 100 * (vy + height)) % height

        if x == width // 2 or y == height // 2:
            continue

        quad_idx = (int(x > width // 2)) + (int(y > height // 2) * 2)
        quads[quad_idx] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
