from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/17
def solution(identifier):
    puzzle_input = parse_file("day17.txt", identifier)
    # Write Solution here

    registers = [
        int(puzzle_input[0].split(": ")[1]),
        int(puzzle_input[1].split(": ")[1]),
        int(puzzle_input[2].split(": ")[1]),
    ]
    program = list(map(int, puzzle_input[4].split(": ")[1].split(",")))

    result = run_program(registers, program)
    return ",".join(map(str, result))


def run_program(registers, program):
    def combo_operand(value):
        match value:
            case 0 | 1 | 2 | 3:
                return value
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C

    A, B, C = registers
    pointer = 0
    outputs = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:  # adv
            A //= 2 ** combo_operand(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = combo_operand(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                pointer = operand
                continue  # skip the pointer increment
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            outputs.append(combo_operand(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** combo_operand(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** combo_operand(operand))

        pointer += 2

    return outputs


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
