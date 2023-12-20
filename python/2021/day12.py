from ..aoc_utils import part_header, highlight, timer_func
from collections import defaultdict


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    network: dict[str, set[str]] = defaultdict(set)

    lines = open(input_file).read().splitlines()

    for i, line in enumerate(lines):
        a, b = line.split("-")
        network[a].add(b)
        network[b].add(a)

    def dfs(node: str, visited: set[str]) -> int:
        if node == "end":
            return 1

        count = 0

        for neighbor in network[node]:
            if neighbor in visited:
                continue

            count += dfs(neighbor, visited | {node} if node.islower() else visited)

        return count

    solution = dfs("start", set())

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 19
    else:
        assert solution == 3779


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    network: dict[str, set[str]] = defaultdict(set)

    lines = open(input_file).read().splitlines()

    for i, line in enumerate(lines):
        a, b = line.split("-")
        network[a].add(b)
        network[b].add(a)

    def dfs(node: str, visited: set[str], small_cave_twice: bool = False) -> int:
        if node == "end":
            return 1

        count = 0

        for neighbor in network[node]:
            if neighbor == "start":
                continue
            if neighbor in visited and small_cave_twice:
                continue
            if neighbor in visited:
                count += dfs(
                    neighbor, visited | {node} if node.islower() else visited, True
                )
            else:
                count += dfs(
                    neighbor,
                    visited | {node} if node.islower() else visited,
                    small_cave_twice,
                )

        return count

    solution = dfs("start", set())

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 103
    else:
        assert solution == 3779
