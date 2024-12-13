from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/5
def solution(identifier):
    puzzle_input = read_file("day5.txt", identifier, split_lines=False)
    # Write Solution here
    rules_input, updates = puzzle_input.split("\n\n")
    rules_input = rules_input.splitlines()
    updates = [u.split(',') for u in updates.splitlines()]

    # load rules into a dictionary based on the first number
    rules = {}
    for rule in rules_input:
        rule = rule.split("|")
        if rules.get(rule[0]) is None:
            rules[rule[0]] = []
        rules[rule[0]].append(rule[1])

    result = 0
    for update in updates:
        update_len = len(update)
        rule_check, incorrectly = check_update(update, rules)

        if rule_check:
            middle = update[update_len // 2]
            result += int(middle)

    return result


def check_update(update, rules):
    update_len = len(update)
    incorrectly = []

    for i in range(update_len):
        for j in range(i + 1, update_len):
            # check if the current page is not in one of the later pages rules
            if update[j] in list(rules.keys()) and update[i] in rules[update[j]]:
                incorrectly = [i, j]
                return False, incorrectly
    return True, incorrectly


def switch_element(inp_list, elements):
    inp_list[elements[0]], inp_list[elements[1]] = inp_list[elements[1]], inp_list[elements[0]]
    return inp_list


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
