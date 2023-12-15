import argparse
import re
from typing import Optional
from aoc_utils import part_header
from collections import defaultdict

sample_input = "inputs/day15/sample.txt"
real_input = "inputs/day15/input.txt"


def hash_string(string: str) -> int:
    this_sum = 0
    for char in string:
        this_sum += ord(char)
        this_sum *= 17
        this_sum = this_sum % 256

    return this_sum


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    steps = open(input_file).read().split(",")
    # for i, step in enumerate(steps):
    # this_hash = hash_string(step)
    # print(f"{i}: {step} -> {this_hash}")
    # solution += this_hash
    # solution += hash_string(step)

    # One-liner
    solution = sum(map(hash_string, steps))

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 1320
    else:
        assert solution == 513172


def find_label(box: list[tuple[str, int]], label_to_find: str) -> Optional[int]:
    for i, (label, length) in enumerate(box):
        if label == label_to_find:
            return i
    return None


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    boxes = defaultdict(list[tuple[str, int]])

    steps = open(input_file).read().split(",")

    def print_boxes(boxes: dict[int, list[tuple[str, int]]]):
        for box in boxes:
            if boxes[box]:
                print(f"\tBox #{box}:\t{boxes[box]}")

    for i, step in enumerate(steps):
        label, *action = re.findall(r"\w+|\S", step)
        box = hash_string(label)
        if len(action) == 2:
            focal_length = int(action[1])
            loc = find_label(boxes[box], label)

            if loc is None:
                boxes[box].append((label, focal_length))
            else:
                boxes[box][loc] = (label, focal_length)

        elif len(action) == 1:
            boxes[box] = [(l, f) for l, f in boxes[box] if l != label]
        else:
            raise ValueError(f"Unknown action: {action}")

    # print_boxes(boxes)

    # solution = 0
    # for box in boxes:
    #     this_sum = 0
    #     for i, (label, length) in enumerate(boxes[box]):
    #         this_sum += (box + 1) * (i + 1) * length
    #     solution += this_sum

    # One-liner
    solution = sum(
        (box + 1) * (i + 1) * length
        for box in boxes
        for i, (label, length) in enumerate(boxes[box])
    )

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 145
    else:
        assert solution == 237806


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
