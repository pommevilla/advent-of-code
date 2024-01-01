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


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    print(f"\n\tNot yet implemented")

    if testing:
        assert solution == 0
    else:
        assert solution == 0
