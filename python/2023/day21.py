from ..aoc_utils import part_header, highlight, timer_func
from collections import deque

adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def print_garden(
    garden: dict[tuple[int, int], tuple[str, set[tuple[int, int]]]],
    v_trees: set[tuple[int, int]],
    v_paths: set[tuple[int, int]],
    height: int,
    width: int,
):
    out_str = ""
    for i in range(height):
        out_str += f"  {i:2}  "
        for j in range(width):
            char = garden[(i, j)][0]
            if (i, j) in v_trees:
                # char = highlight(char, "green")
                char = char
            elif (i, j) in v_paths:
                char = highlight("O", "blue")
            out_str += f"{char} "
        out_str += "\n"
    print(out_str)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = open(input_file).read().splitlines()

    nodes = {}
    height = len(lines)
    width = len(lines[0])

    for i, line in enumerate(lines):
        # print(f"{i}: {line}")
        for j, char in enumerate(line):
            # print(f"{i}, {j}: {char}")
            nodes[(i, j)] = (char, set())
            if char == "S":
                starting_pos = (i, j)
                nodes[(i, j)] = (".", set())
            for adj in adjacents:
                x = i + adj[0]
                y = j + adj[1]
                if 0 <= x < height and 0 <= y < width:
                    nodes[(i, j)][1].add((x, y))

    # Could just do height = i, but this is more readable imo

    visited_paths = {starting_pos}
    visited_trees = set()
    answer = set()

    max_steps = 64

    bfs = deque([(starting_pos, max_steps)])

    while bfs:
        pos, steps = bfs.popleft()

        if steps % 2 == 0:
            answer.add(pos)

        if steps == 0:
            continue

        for adj in adjacents:
            new_row = pos[0] + adj[0]
            new_col = pos[1] + adj[1]
            if 0 <= new_row < height and 0 <= new_col < width:
                if (
                    nodes[(new_row, new_col)][0] == "."
                    and (new_row, new_col) not in visited_paths
                ):
                    visited_paths.add((new_row, new_col))
                    bfs.append(((new_row, new_col), steps - 1))

    print_garden(nodes, visited_trees, answer, height, width)

    solution = len(answer)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 16
    else:
        assert solution == 3658


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()

    nodes = {}
    height = len(lines)
    width = len(lines[0])

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            nodes[(i, j)] = (char, set())
            if char == "S":
                starting_pos = (i, j)
                nodes[(i, j)] = (".", set())
            for adj in adjacents:
                x = i + adj[0]
                y = j + adj[1]
                if 0 <= x < height and 0 <= y < width:
                    nodes[(i, j)][1].add((x, y))

    visited_paths = {starting_pos}
    visited_trees = set()
    answer = set()

    max_steps = 10

    bfs = deque([(starting_pos, max_steps)])

    while bfs:
        pos, steps = bfs.popleft()

        if steps % 2 == 0:
            answer.add(pos)

        if steps == 0:
            continue

        for adj in adjacents:
            new_row = pos[0] + adj[0]
            new_col = pos[1] + adj[1]
            if 0 <= new_row < height and 0 <= new_col < width:
                if (
                    nodes[(new_row, new_col)][0] == "."
                    and (new_row, new_col) not in visited_paths
                ):
                    visited_paths.add((new_row, new_col))
                    bfs.append(((new_row, new_col), steps - 1))

    solution = len(answer)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 0
    else:
        assert solution == 0
