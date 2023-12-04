import argparse
from aoc_utils import part_header
from itertools import zip_longest

sample_input = "inputs/day4/sample.txt"
real_input = "inputs/day4/input.txt"


@part_header(part=1)
def part_1(input_file: str, test: bool = False):
    sum = 0

    with open(input_file) as fin:
        for line in fin:
            winning_numbers, our_numbers = (
                set(int(n) for n in l.split()) for l in line.split(":")[1].split("|")
            )
            matches = len(winning_numbers & our_numbers)
            sum += 2 ** (matches - 1) if matches > 0 else 0

    print(f"\n\tSolution: {sum}")

    if test:
        assert sum == 13
    else:
        assert sum == 25010


# For adding the num_tickets lists, which will likely be mismatched in size.
def list_adder(l1: list[int], l2: list[int]) -> list[int]:
    return [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    sum = 0
    num_tickets = []

    with open(input_file) as fin:
        for i, line in enumerate(fin):
            winning_numbers, our_numbers = (
                set(int(n) for n in l.split()) for l in line.split(":")[1].split("|")
            )
            matches = len(winning_numbers & our_numbers)

            if num_tickets:
                num_tickets[0] += 1
            else:
                num_tickets.append(1)

            sum += num_tickets[0]
            new_tickets = [1] if not num_tickets else [1 * num_tickets.pop(0)] * matches
            num_tickets = list_adder(num_tickets, new_tickets)

            # print(f"Card {i}: Found {matches} matches")
            # print(f"\tadding {matches} copies: {num_tickets}")
            # print(f"\tsum: {sum}")

    print(f"\n\tSolution: {sum}")

    if testing:
        assert sum == 30
    else:
        assert sum == 9924412


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
