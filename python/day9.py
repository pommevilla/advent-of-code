import argparse
from aoc_utils import part_header
from itertools import pairwise

sample_input = "inputs/day9/sample.txt"
real_input = "inputs/day9/input.txt"


def find_next_number(seq: list[int]) -> int:
    diff = find_diff(seq)
    return seq[-1] + diff


def find_diff(seq: list[int], level: int = 0) -> int:
    diffs = [y - x for x, y in pairwise(seq)]
    # print("{}{}".format("    " * level, "   ".join([str(x) for x in seq])))
    if all(diff == 0 for diff in diffs):
        return 0
    else:
        return diffs[-1] + find_diff(diffs, level + 1)


def read_seqs(input_file: str) -> list[list[int]]:
    seqs = [
        [int(x) for x in line.strip().split()] for line in open(input_file).readlines()
    ]
    return seqs


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    seqs = read_seqs(input_file)

    solution = sum([find_next_number(seq) for seq in seqs])

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 114
    else:
        assert solution == 2043677056


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    seqs = read_seqs(input_file)

    solution = sum([find_next_number(seq[::-1]) for seq in seqs])

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 2
    else:
        assert solution == 1062


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
