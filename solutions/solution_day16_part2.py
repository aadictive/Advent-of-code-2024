from constants import *
from utility.parseFile import *


# Problem Statement: https://adventofcode.com/2024/day/16
def solution(identifier):
    puzzle_input = parse_file("day16.txt", identifier)
    # Write Solution here
    grid = [list(row) for row in puzzle_input]
    possible_routes = find_routes(grid)

    min_score = min(r[1] for r in possible_routes)
    best_routes = [r for r in possible_routes if r[1] == min_score]

    tiles = {tile for route in best_routes for tile in route[0]}
    return len(tiles)


def find_routes(grid):
    rows, cols = len(grid), len(grid[0])
    start = None
    end = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "S":
                start = (y, x)
            elif grid[y][x] == "E":
                end = (y, x)
        if start and end:
            break

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visited = {}

    queue = [(start, [start], 0, 0)]  # (y, x), history, score, direction
    while queue:
        (y, x), history, curr_score, curr_dir = queue.pop(0)

        if (y, x) == end:
            routes.append((history, curr_score))
            continue

        if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
            continue

        visited[((y, x), curr_dir)] = curr_score

        for _dir, (dy, dx) in enumerate(dirs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] != "#" and (ny, nx) not in history:
                if _dir == curr_dir:
                    queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))  # move forward
                else:
                    queue.append(((y, x), history + [], curr_score + 1000, _dir))  # turn

    return routes


def execute_example_file():
    return solution(EXAMPLE_FILE_IDENTIFIER)


def execute_puzzle_file():
    return solution(PUZZLE_FILE_IDENTIFIER)
