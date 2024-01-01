from ..aoc_utils import part_header, highlight, timer_func
from heapq import heappop, heappush
from collections import defaultdict
from math import inf

adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    grid = [list(map(int, line)) for line in open(input_file).read().split()]

    risk_map: dict[tuple[int, int], int] = {}

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            risk_map[(i, j)] = char

    end = (len(grid) - 1, len(grid[0]) - 1)
    pq = [(0, 0, 0)]
    visited: dict[tuple[int, int], int] = {}

    while len(pq) > 0:
        x, y, risk_factor = heappop(pq)
        if (x, y) == end:
            solution = visited[(x, y)]
        for adj in adjacents:
            new_x = x + adj[0]
            new_y = y + adj[1]
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                new_risk = risk_factor + risk_map[(new_x, new_y)]
                if new_risk < visited.get((new_x, new_y), inf):
                    visited[(new_x, new_y)] = new_risk
                    heappush(pq, (new_x, new_y, new_risk))

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 40
    else:
        assert solution == 373


def print_risk_map(risk_map: dict[tuple[int, int], int], size: int):
    for i in range(size):
        for j in range(size):
            print(risk_map[(i, j)], end="")
        print()


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    grid = [list(map(int, line)) for line in open(input_file).read().split()]
    size = len(grid)

    risk_map: dict[tuple[int, int], int] = {
        (a * size + i, b * size + j): (x + a + b - 1) % 9 + 1
        for i, row in enumerate(grid)
        for j, x in enumerate(row)
        for a in range(5)
        for b in range(5)
    }

    end = (size * 5 - 1, size * 5 - 1)
    pq = [(0, 0, 0)]
    visited: dict[tuple[int, int], int] = {}

    while len(pq) > 0:
        x, y, risk_factor = heappop(pq)
        if (x, y) == end:
            solution = visited[(x, y)]
        for adj in adjacents:
            new_x = x + adj[0]
            new_y = y + adj[1]
            if 0 <= new_x < len(grid) * 5 and 0 <= new_y < len(grid[0]) * 5:
                new_risk = risk_factor + risk_map[(new_x, new_y)]
                if new_risk < visited.get((new_x, new_y), inf):
                    visited[(new_x, new_y)] = new_risk
                    heappush(pq, (new_x, new_y, new_risk))

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 315
    else:
        assert solution == 2868
