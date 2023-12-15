import argparse
from ..aoc_utils import part_header
from collections import deque

sample_input = "inputs/day10/sample.txt"
real_input = "inputs/day10/input.txt"

dirs = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

pipes = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
    ".": (0, 0),
}

pipe_chars = dict(zip("-|F7LJ", "═║╔╗╚╝"))

nodes = {}


# Create a node class with addition
class Node:
    def __init__(self, node: tuple[int, int]):
        self.node = node

    def __add__(self, other: tuple[int, int]) -> tuple[int, int]:
        return tuple(x + y for x, y in zip(self.node, other))


def add_nodes(node_1: tuple[int, int], node_2: tuple[int, int]) -> tuple[int, int]:
    return tuple(x + y for x, y in zip(node_1, node_2))


def get_neighbors(starting_node: tuple[int, int], pipe: str) -> tuple[int, int]:
    neighbors = []

    if pipe != ".":
        for direction in pipes[pipe]:
            neighbors.append(add_nodes(starting_node, dirs[direction]))

    return neighbors


def get_starting_nodes(
    starting_pipe_node: tuple[int, int], nodes: dict[tuple[int, int], tuple[int, int]]
) -> list[tuple[int, int]]:
    adjacent_nodes = [
        (starting_pipe_node[0] + 1, starting_pipe_node[1]),
        (starting_pipe_node[0] - 1, starting_pipe_node[1]),
        (starting_pipe_node[0], starting_pipe_node[1] + 1),
        (starting_pipe_node[0], starting_pipe_node[1] - 1),
    ]

    # print(f"Starting pipe: {starting_pipe_node}")

    height = max(nodes, key=lambda x: x[0])[0]
    width = max(nodes, key=lambda x: x[1])[1]
    neighbors = []
    for adj_node in adjacent_nodes:
        if (
            adj_node[0] >= 0
            and adj_node[1] < height
            and adj_node[1] >= 0
            and adj_node[1] < width
        ) and starting_pipe_node in nodes[adj_node]:
            neighbors.append(adj_node)
    # print(f"{adjacent_nodes=}")
    # print(f"{neighbors=}")
    return neighbors


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = [line.strip() for line in open(input_file).readlines()]
    for i, line in enumerate(lines):
        # print(f"Line {i}:")
        for j, char in enumerate(line):
            if char == "S":
                starting_pipe = (i, j)
            else:
                nodes[(i, j)] = get_neighbors((i, j), char)
            # print(f"\t{j}: {char}")

    starting_nodes = get_starting_nodes(starting_pipe, nodes)
    bfs = deque([(starting_node, 1) for starting_node in starting_nodes])
    distances = {starting_pipe: 0}

    print(f"Starting at {starting_nodes}")
    while bfs:
        current_node, current_distance = bfs.popleft()
        # print(f"Current_node: {current_node}")
        if current_node in distances:
            continue
        distances[current_node] = current_distance
        for neighbor in nodes[current_node]:
            # print(f"\tAdding {neighbor}")
            bfs.append((neighbor, current_distance + 1))
        # print(f"{distances=}")

    # for k in nodes:
    #     print(f"{k}: {nodes[k]}")

    solution = max(distances.values())
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 8
    else:
        assert solution == 0


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    print(f"\n\tNot yet implemented")

    if testing:
        assert solution == 0
    else:
        assert solution == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
