from ..aoc_utils import part_header


def transpose(grid: list[list[str]]) -> list[list[str]]:
    return [list(x) for x in zip(*grid)]


def slide_west(grid: list[list[str]]) -> list[list[str]]:
    for row in grid:
        slot = 0
        for i, char in enumerate(row):
            if char == "#":
                slot = i + 1
            if char == "O":
                row[i] = "."
                row[slot] = "O"
                slot += 1
    return grid


def print_lines(lines: list[list[str]]):
    for line in lines:
        print("".join(line))


def score_grid(grid: list[list[str]]) -> int:
    this_score = 0
    height = len(grid[0])
    for i, line in enumerate(grid):
        line_sum = 0
        for j, char in enumerate(line):
            if char == "O":
                line_sum += height - j
        this_score += line_sum
    return this_score


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = transpose(open(input_file).read().splitlines())
    lines = slide_west(lines)

    solution = score_grid(lines)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 136
    else:
        assert solution == 106997


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()

    cache = {}

    i = 0
    directions = "NWSE"
    NUM_CYCLES = 1000000000
    while i < NUM_CYCLES:
        grid_cfg = "\n".join("".join(line) for line in lines)
        if grid_cfg in cache:
            # print(f"Found repeat at cycle {i}, dir {directions[i % 4]}")
            cycle = i - cache[grid_cfg]
            i += (NUM_CYCLES - i) // cycle * cycle
            if i == NUM_CYCLES:
                break

        cache[grid_cfg] = i

        # Tilting north
        lines = transpose(lines)
        lines = slide_west(lines)

        # Tilting west
        # This untransposes the grid which was previously oriented West,
        # orienting it North again
        lines = transpose(lines)
        lines = slide_west(lines)

        # Tilting south
        lines = lines[::-1]
        lines = transpose(lines)
        lines = slide_west(lines)

        # Tilting east
        lines = transpose(lines)
        lines = lines[::-1]
        lines = [line[::-1] for line in lines]
        lines = slide_west(lines)

        # Reorient to North
        lines = [line[::-1] for line in lines]

        # print(f"======== Cycle {i} ========")
        # print_lines(lines)
        i += 1

    # Need to transpose again since the score_grid function expects
    # it to be oriented West
    lines = transpose(lines)

    solution = score_grid(lines)
    print(f"\n\tSolution: {solution}")
    if testing:
        assert solution == 64
    else:
        assert solution == 99641
