from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/14
def solution(identifier):
    puzzle_input = parse_file("day14.txt", identifier)
    # Write Solution here
    robots = []
    for line in puzzle_input:
        a, b = line.split(" ")
        x, y = map(int, a[2:].split(","))
        vx, vy = map(int, b[2:].split(","))
        robots.append(((x, y), (vx, vy)))

    width = 101
    height = 103

    t = 0

    while True:
        t += 1
        pos = set()
        valid = True

        for (x, y), (vx, vy) in robots:
            x = (x + t * (vx + width)) % width
            y = (y + t * (vy + height)) % height
            if (x, y) in pos:
                valid = False
                break
            pos.add((x, y))

        if valid:
            return t


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
