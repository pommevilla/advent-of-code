from ..aoc_utils import part_header


def get_node_dict(nodes: list[list[str]]) -> dict[str, list[str]]:
    node_dict = {
        k: v[1:-1].split(", ")
        for k, v in [node.split(" = ") for node in nodes.split("\n")]
    }

    return node_dict


def next_step(
    node_dict: dict[str, list[str]], current_node: str, current_step: str
) -> str:
    if current_step == "R":
        return node_dict[current_node][1]
    else:
        return node_dict[current_node][0]


def get_walk_length(
    node_dict: dict[str, list[str]], current_node: str, steps: str
) -> int:
    step_number = 0
    while current_node[-1] != "Z":
        current_step = steps[step_number % len(steps)]
        current_node = next_step(node_dict, current_node, current_step)
        # print(f" {current_node}")
        step_number += 1
    return step_number


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    # input_file = "inputs/day8/sample1.txt"
    solution = 0

    steps, nodes = open(input_file).read().split("\n\n")
    nodes = get_node_dict(nodes)

    current_node = "AAA"
    step_number = 0
    while current_node != "ZZZ":
        current_step = steps[step_number % len(steps)]
        # print(f"{step_number}: {current_node}[{current_step}] ->", end="")
        current_node = next_step(nodes, current_node, current_step)
        # print(f" {current_node}")
        step_number += 1

    print(f"\n\tSolution: {step_number}")

    solution = step_number

    if testing:
        assert solution == 2
    else:
        assert solution == 24253


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    from math import lcm

    if testing:
        input_file = "inputs/2023/day8/sample2.txt"

    solution = 0

    steps, nodes = open(input_file).read().split("\n\n")
    nodes = get_node_dict(nodes)

    starting_nodes = [node for node in nodes if node[-1] == "A"]
    walk_lengths = [get_walk_length(nodes, node, steps) for node in starting_nodes]
    min_walk_length = lcm(*walk_lengths)

    solution = min_walk_length

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 6
    else:
        assert solution == 12357789728873
