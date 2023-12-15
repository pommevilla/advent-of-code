from ..aoc_utils import part_header
from math import sqrt


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
        assert answer == 33875953
