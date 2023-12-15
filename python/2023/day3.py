from ..aoc_utils import part_header
import re


@part_header(part=1)
def part_1(input_file: str, test: bool = False):
    sum = 0

    with open(input_file) as fin:
        lines = [line.strip() for line in fin.readlines()]

    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            # Adding cells to the left and right of the digits to look at
            adjacent_idxs = [(i, match.start() - 1), (i, match.end())]

            # Adding cells above and below the digits to look at
            adjacent_idxs += [
                (i - 1, j) for j in range(match.start() - 1, match.end() + 1)
            ]
            adjacent_idxs += [
                (i + 1, j) for j in range(match.start() - 1, match.end() + 1)
            ]

            # For each adjacent cell, check if there's a non-"." character and if its
            # within bounds
            for a, b in adjacent_idxs:
                if (
                    0 <= a < len(lines)
                    and 0 <= b < len(lines[a])
                    and lines[a][b] != "."
                ):
                    # If we find one, add it to the sum and break the loop
                    # print(f"\t{a}, {b}: {lines[a][b]}")
                    # print(f"Adding {match.group()} to sum")
                    sum += int(match.group())
                    break

    print(f"\n\tSolution: {sum}")

    if test:
        assert sum == 4361
    else:
        assert sum == 546312


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    from collections import defaultdict

    sum = 0

    # We'll keep track of which digits are adjacent to which symbols
    adjacent_symbols = defaultdict(list)

    with open(input_file) as fin:
        lines = [line.strip() for line in fin.readlines()]

    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            adjacent_idxs = [(i, match.start() - 1), (i, match.end())]
            adjacent_idxs += [
                (i - 1, j) for j in range(match.start() - 1, match.end() + 1)
            ]
            adjacent_idxs += [
                (i + 1, j) for j in range(match.start() - 1, match.end() + 1)
            ]

            # If we find * in an adjacent cell, record the digit in the
            # adjacent_symbols entry for the * position
            for a, b in adjacent_idxs:
                if (
                    0 <= a < len(lines)
                    and 0 <= b < len(lines[a])
                    and lines[a][b] == "*"
                ):
                    adjacent_symbols[(a, b)].append(match.group())

    for k, v in adjacent_symbols.items():
        if len(v) == 2:
            sum += int(v[0]) * int(v[1])

    print(f"\n\tSolution: {sum}")

    if testing:
        assert sum == 467835
    else:
        assert sum == 87449461
