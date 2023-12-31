from ..aoc_utils import part_header
from itertools import combinations


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = [line.strip() for line in open(input_file).readlines()]

    galaxies = []
    double_cols = [_ for _ in range(len(lines[0]))]

    doubled_rows = 0

    for i, line in enumerate(lines):
        # print(line)
        if "#" not in line:
            doubled_rows += 1
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i + doubled_rows, j))
                if j in double_cols:
                    double_cols.remove(j)

    galaxies = [
        (g[0], g[1] + sum([1 for col in double_cols if col < g[1]])) for g in galaxies
    ]

    for i, (s, f) in enumerate(combinations(galaxies, 2)):
        dist = abs(s[0] - f[0]) + abs(s[1] - f[1])
        solution += dist

    # print(galaxies)
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 374
    else:
        assert solution == 9795148


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = [line.strip() for line in open(input_file).readlines()]

    galaxies = []
    double_cols = [_ for _ in range(len(lines[0]))]

    doubled_rows = 0

    for i, line in enumerate(lines):
        # print(line)
        if "#" not in line:
            doubled_rows += 1
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i + (doubled_rows * (1000000 - 1)), j))
                if j in double_cols:
                    double_cols.remove(j)

    galaxies = [
        (g[0], g[1] + (sum([1 for col in double_cols if col < g[1]]) * (1000000 - 1)))
        for g in galaxies
    ]

    for i, (s, f) in enumerate(combinations(galaxies, 2)):
        dist = abs(s[0] - f[0]) + abs(s[1] - f[1])
        solution += dist

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 82000210
    else:
        assert solution == 650672493820
