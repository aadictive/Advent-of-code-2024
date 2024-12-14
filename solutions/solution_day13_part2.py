from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/X
def solution(identifier):
    puzzle_input = read_file("day13.txt", identifier)
    # Write Solution here
    machines = ("\n".join(puzzle_input)).split("\n\n")
    coins = 0

    for machine in machines:
        btn_a, btn_b, prize = machine.split("\n")

        btn_a = [*map(lambda i: int(i[2:]), btn_a.split(": ")[1].split(", "))]
        btn_b = [*map(lambda i: int(i[2:]), btn_b.split(": ")[1].split(", "))]
        prize = [*map(lambda i: int(i[2:]) + 10000000000000, prize.split(": ")[1].split(", "))]

        times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1])
        times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]

        if times_a.is_integer() and times_b.is_integer():
            coins += int(times_a) * 3 + int(times_b)

    return coins


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
