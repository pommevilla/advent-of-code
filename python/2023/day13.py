from ..aoc_utils import part_header
from typing import Optional


def find_reflection(lines: list[str]) -> Optional[int]:
    for i in range(1, len(lines)):
        if all(a == b for a, b in zip(lines[i:], lines[:i][::-1])):
            return i


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0
    lines = open(input_file).read().split("\n\n")

    for i, pattern in enumerate(lines):
        pattern = pattern.splitlines()
        if horizontal_reflection := find_reflection(pattern):
            solution += 100 * horizontal_reflection
        elif vertical_reflection := find_reflection([*zip(*pattern)]):
            solution += vertical_reflection

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 405
    else:
        assert solution == 35360


def find_new_reflection(lines: list[str]) -> Optional[int]:
    for i in range(1, len(lines)):
        difference = sum(
            ia != ib for a, b in zip(lines[i:], lines[:i][::-1]) for ia, ib in zip(a, b)
        )
        if difference == 1:
            return i


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().split("\n\n")

    for i, pattern in enumerate(lines):
        pattern = pattern.splitlines()
        if horizontal_reflection := find_new_reflection(pattern):
            # print(f"Found new horizontal reflection at {horizontal_reflection}")
            solution += 100 * horizontal_reflection
        elif vertical_reflection := find_new_reflection([*zip(*pattern)]):
            # print(f"Found new vertical reflection at {vertical_reflection}")
            solution += vertical_reflection

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 400
    else:
        assert solution == 36755
