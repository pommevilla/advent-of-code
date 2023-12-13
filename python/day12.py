import argparse
from aoc_utils import part_header

sample_input = "inputs/day12/sample.txt"
real_input = "inputs/day12/input.txt"


cache = {}


def count_solutions(springs: str, groups: list[int]) -> int:
    if not springs:
        return 1 if not groups else 0

    if not groups:
        return 0 if "#" in springs else 1

    if sum(groups) > len(springs):
        return 0

    key = (springs, tuple(groups))
    if key in cache:
        return cache[key]

    count = 0

    if springs[0] == ".":
        count += count_solutions(springs[1:], groups)
    elif springs[0] == "?":
        count += count_solutions("#" + springs[1:], groups)
        count += count_solutions("." + springs[1:], groups)
    else:
        if (
            # The initial group is long enough
            len(springs) >= groups[0]
            # There aren't any non-springs in the initial group
            and "." not in springs[: groups[0]]
            # The character after the initial group isn't another string
            and (groups[0] == len(springs) or springs[groups[0]] != "#")
        ):
            count += count_solutions(springs[groups[0] + 1 :], groups[1:])

    cache[key] = count
    return count


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = [line.strip() for line in open(input_file).readlines()]

    for i, line in enumerate(lines):
        springs, groups = line.split()
        groups = [int(x) for x in groups.split(",")]
        print(f"{springs} -> {groups}")
        solutions_found = count_solutions(springs, groups)
        print(f"\tFound {solutions_found} solutions\n")
        solution += solutions_found

    # print(lines)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 21
    else:
        assert solution == 7221


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = [line.strip() for line in open(input_file).readlines()]

    for i, line in enumerate(lines):
        springs, groups = line.split()
        print(f"{springs} -> {groups}")
        springs = "?".join([springs] * 5)
        groups = [int(x) for x in groups.split(",")] * 5
        solutions_found = count_solutions(springs, groups)
        print(f"\tFound {solutions_found} solutions\n")
        solution += solutions_found

    print(f"\tSolution: {solution}")

    if testing:
        assert solution == 525152
    else:
        assert solution == 7139671893722


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
