from ..aoc_utils import part_header, highlight
from collections import deque

adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_low_point(grid: list[list[int]], pos: tuple[int, int]) -> bool:
    x, y = pos
    for dx, dy in adjacents:
        if is_in_bounds(grid, (x + dx, y + dy)):
            if grid[x + dx][y + dy] <= grid[x][y]:
                return False
    return True


def is_in_bounds(grid: list[list[int]], pos: tuple[int, int]) -> bool:
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def print_low_points(grid: list[list[int]], low_points: set[tuple[int, int]]):
    out_str = "\n"
    for i, line in enumerate(grid):
        out_str += f"\t{i:}\t"
        for j, char in enumerate(line):
            if (i, j) in low_points:
                char = highlight(char, "blue", padding=2)
            out_str += f"{char:2}"
        out_str += "\n"
    print(out_str)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lava_map = [list(map(int, line)) for line in open(input_file).read().splitlines()]

    low_points: set[tuple[int, int]] = set()

    for i, line in enumerate(lava_map):
        for j, char in enumerate(line):
            if is_low_point(lava_map, (i, j)):
                low_points.add((i, j))
                solution += char + 1

    print_low_points(lava_map, low_points)
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 15
    else:
        assert solution == 537


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 1

    lava_map = [list(map(int, line)) for line in open(input_file).read().splitlines()]

    low_points: set[tuple[int, int]] = set()

    for i, line in enumerate(lava_map):
        for j, char in enumerate(line):
            if is_low_point(lava_map, (i, j)):
                low_points.add((i, j))

    basin_sizes = []
    basin_points = set()
    for low_point in low_points:
        bfs = deque([low_point])
        basin = set()
        while bfs:
            (x, y) = bfs.popleft()
            basin_points.add((x, y))
            for dx, dy in adjacents:
                if is_in_bounds(lava_map, (x + dx, y + dy)):
                    if (
                        lava_map[x + dx][y + dy] > lava_map[x][y]
                        and lava_map[x + dx][y + dy] != 9
                    ):
                        basin.add((x + dx, y + dy))
                        bfs.append((x + dx, y + dy))
        basin_sizes.append(len(basin) + 1)

    three_largest = sorted(basin_sizes)[-3:]

    for size in three_largest:
        solution *= size

    print_low_points(lava_map, basin_points)
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 1134
    else:
        assert solution == 1142757
