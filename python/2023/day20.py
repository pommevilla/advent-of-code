from ..aoc_utils import part_header, highlight, timer_func


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    nodes = open(input_file).read().splitlines()

    network = {}

    for i, node in enumerate(nodes):
        # print(f"{i}: {node}")
        node, neighbors = node.split(" -> ")
        if node == "broadcaster":
            broadcaster_neighbors = neighbors.split(", ")
        else:
            node_type = node[0]
            node_name = node[1:]
            neighbors = neighbors.split(", ")
            # print(f"\t{node} conects to: {neighbors}")
            network[node_name] = (node_type, neighbors)

    print(broadcaster_neighbors)

    for k, v in network.items():
        print(f"{k} -> {v}")

    print(f"\n\tSolution: {solution}")

    def press_button(
        broadcaster_neighbors: list[str],
        broadcast_network: dict[str, tuple[str, list[str]]],
    ):
        for neighbor in broadcaster_neighbors:
            give_pulse(neighbor, "low")
            print(f"{neighbor} receives low pulse")

    def give_pulse(node: str, pulse_type: str):

    for _ in range(10):
        press_button(broadcaster_neighbors, network)

    if testing:
        assert solution == 0
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
