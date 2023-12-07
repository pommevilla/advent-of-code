import argparse
from aoc_utils import part_header

sample_input = "inputs/day6/sample.txt"
real_input = "inputs/day6/input.txt"


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 28
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
