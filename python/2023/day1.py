from ..aoc_utils import part_header


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
def part_2(input: str, testing: bool):
    if testing:
        input = "inputs/2023/day1/day1_sample2.txt"

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
