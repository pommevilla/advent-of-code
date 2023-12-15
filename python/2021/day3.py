from ..aoc_utils import part_header
from collections import Counter

directions = {"forward": 1, "down": 1, "up": -1}


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0
    report = open(input_file).read().splitlines()

    positions = {}

    width = len(report[0])

    for i in range(width):
        positions[i] = Counter([line[i] for line in report])

    gamma = "".join([positions[pos].most_common(1)[0][0] for pos in positions])
    epsilon = "".join(["1" if x == "0" else "0" for x in gamma])

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    solution = gamma * epsilon

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 198
    else:
        assert solution == 3895776


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    report = open(input_file).read().splitlines()

    width = len(report[0])

    lines = report
    for i in range(width):
        if len(lines) == 1:
            break
        position_count = Counter([line[i] for line in lines])
        if position_count.most_common(1)[0][1] == position_count.most_common(2)[1][1]:
            most_common = "1"
        else:
            most_common = position_count.most_common(1)[0][0]
        lines = [line for line in lines if line[i] == most_common]

    oxygen_rating = int(lines[0], 2)

    lines = report
    for i in range(width):
        if len(lines) == 1:
            break
        position_count = Counter([line[i] for line in lines])
        if position_count.most_common(2)[1][1] == position_count.most_common(2)[0][1]:
            least_common = "0"
        else:
            least_common = position_count.most_common(2)[1][0]
        lines = [line for line in lines if line[i] == least_common]

    scrubber_rating = int(lines[0], 2)

    print(f"Oxygen Rating: {oxygen_rating}")
    print(f"Scrubber Rating: {scrubber_rating}")

    solution = oxygen_rating * scrubber_rating

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 230
    else:
        assert solution == 1759818555
