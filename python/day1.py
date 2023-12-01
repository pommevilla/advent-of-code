import argparse
from aoc_utils import part_header

sample_input = "inputs/day1_sample.txt"
real_input = "inputs/day1.txt"


def get_first_number(line: str):
    for x in line:
        if x.isdigit():
            return int(x)


@part_header(part=1)
def part_1(input: str, test: bool = False):
    sum = 0
    with open(input) as fin:
        for line in fin:
            first_num = get_first_number(line)
            last_num = get_first_number(line[::-1])
            sum += first_num * 10 + last_num
    print(f"\tSolution: {sum}")

    if test:
        assert sum == 142


@part_header(part=2)
def part_2(testing: bool):
    if testing:
        input = "inputs/day1_sample2.txt"
    else:
        input = "inputs/day1.txt"

    number_strings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    with open(input) as fin:
        sum = 0
        for line in fin:
            nums = []
            for i, x in enumerate(line):
                if x.isdigit():
                    nums.append(int(x))
                    continue
                else:
                    for key, value in number_strings.items():
                        if line[i:].startswith(key):
                            nums.append(int(value))

            sum += nums[0] * 10 + nums[-1]

    print(f"\tSolution: {sum}")

    if testing:
        assert sum == 281


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file)
    part_2(args.test)
