from ..aoc_utils import part_header

directions = {"forward": 1, "down": 1, "up": -1}


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0
    horizontal = 0
    vertical = 0

    course = open(input_file).read().splitlines()
    for step in course:
        dir, mag = step.split()
        if dir == "forward":
            horizontal += int(mag)
        else:
            vertical += directions[dir] * int(mag)

    solution = horizontal * vertical

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 150
    else:
        assert solution == 1648020


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0
    horizontal = 0
    aim = 0
    vertical = 0

    course = open(input_file).read().splitlines()
    for step in course:
        dir, mag = step.split()
        if dir == "forward":
            horizontal += int(mag)
            vertical += aim * int(mag)
        else:
            aim += directions[dir] * int(mag)

    solution = horizontal * vertical

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 900
    else:
        assert solution == 1759818555
