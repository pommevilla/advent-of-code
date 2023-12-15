from ..aoc_utils import part_header


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    readings = [int(x) for x in open(input_file).read().splitlines()]

    count = 0

    for i in range(1, len(readings)):
        if readings[i] > readings[i - 1]:
            count += 1

    solution = count

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 7
    else:
        assert solution == 1292


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    readings = [int(x) for x in open(input_file).read().splitlines()]

    count = 0

    for i in range(3, len(readings)):
        if sum(readings[(i - 3) : i]) > sum(readings[(i - 4) : (i - 1)]):
            count += 1

    solution = count

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 5
    else:
        assert solution == 0
