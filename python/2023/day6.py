import argparse
from ..aoc_utils import part_header

sample_input = "inputs/day6/sample.txt"
real_input = "inputs/day6/input.txt"


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    time, distance = [
        [int(x) for x in x.split(":")[1].split()]
        for x in open(input_file).read().split("\n")
    ]

    answer = 1
    for t, d in zip(time, distance):
        winners = 0
        for i in range(t):
            if (t - i) * i > d:
                winners += 1
        answer *= winners

    print(f"\n\tSolution: {answer}")

    if testing:
        assert answer == 288
    else:
        assert answer == 281600


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    time, distance = [
        int(x.split(":")[1].replace(" ", ""))
        for x in open(input_file).read().split("\n")
    ]

    answer = 0

    for i in range(time):
        if (time - i) * i > distance:
            answer += 1

    print(f"\n\tSolution: {answer}")

    if testing:
        assert answer == 71503
    else:
        assert answer == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
