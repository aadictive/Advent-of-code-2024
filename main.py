from solutions import *
import os, sys

base_path = "solutions/"


def print_solution(day, part):
    if int(part) < 3:
        file_path = os.path.join(base_path, f"solution_day{day}_part{part}.py")
        if os.path.exists(file_path):
            print("#########################################")
            print(f"Solution Day {day} Part {part} (example):",
                  eval(f"solution_day{day}_part{part}.execute_example_file()"))
            print(f"Solution Day {day} Part {part} (puzzle):",
                  eval(f"solution_day{day}_part{part}.execute_puzzle_file()"))
            print("#########################################")
    elif int(part) == 3:
        for part in range(1, 3):
            file_path = os.path.join(base_path, f"solution_day{day}_part{part}.py")
            if os.path.exists(file_path):
                print("#########################################")
                print(f"Solution Day {day} Part {part} (example):",
                      eval(f"solution_day{day}_part{part}.execute_example_file()"))
                print(f"Solution Day {day} Part {part} (puzzle):",
                      eval(f"solution_day{day}_part{part}.execute_puzzle_file()"))
                print("#########################################")
    else:
        print("Invalid Selection!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        selection = sys.argv[1]
        day = sys.argv[2]
        part = sys.argv[3]
    else:
        print("###############################################################")
        print(" Welcome to Advent of Code 2024 solutions by Aditya Chaudhari ")
        print("###############################################################")
        print("Select appropriate option to run the solution:")
        print("\t1 - Run all available solutions and print answers.\n\t2 - Run a particular solution.\n\t0 - Exit!")
        usr_selection = input("Enter your value: ")
        if usr_selection == "1":
            selection = "all"
        elif usr_selection == "2":
            selection = "particular"
            day = input("Run solution for which day? (Select between 1-25): ")
            print("Run solution for which part?\n\t1 - Part 1\n\t2 - Part 2\n\t3 - Both parts!\n\t0- Exit!")
            part = input("Enter your value: ")
            if part == "0":
                print("Exiting gracefully!")
                exit(0)
        elif usr_selection == "0":
            print("Exiting gracefully!")
            exit(0)
        else:
            print("Invalid Selection!")
            exit()

    match selection:
        case "all":
            for day in range(1, 26):
                print_solution(day, 3)
        case "particular":
            print_solution(day, part)
