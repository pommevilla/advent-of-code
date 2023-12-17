from ..aoc_utils import part_header, highlight
from collections import Counter


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    with open(input_file) as fin:
        if testing:
            states = list(map(int, fin.readline().split(":")[1].strip().split(",")))
        else:
            states = list(map(int, fin.readline().strip().split(",")))

    days = 80

    current_day = 0
    while current_day < days:
        num_fish = len(states)
        for i in range(num_fish):
            if states[i] == 0:
                states.append(8)
                states[i] = 6
            else:
                states[i] -= 1

        current_day += 1

    # print(states)
    solution = len(states)
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 5934
    else:
        assert solution == 351188


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    with open(input_file) as fin:
        if testing:
            states = list(map(int, fin.readline().split(":")[1].strip().split(",")))
        else:
            states = list(map(int, fin.readline().strip().split(",")))

    days = 256

    # Counter method
    states = Counter(states)
    for i in range(days):
        states = Counter({state - 1: count for state, count in states.items()})
        # All the day 0 fish will be -1 now; add an equal number of new fish
        # starting at 8 and reset the -1 fish to 6
        states[8] += states[-1]
        states[6] += states[-1]

        # Remove the -1 states
        del states[-1]

    # Math method
    # TODO: Figure out recurrence solution

    solution = sum(states.values())
    print(f"\n\tSolution: {solution}")

    if testing:
        if days == 18:
            assert solution == 26
        elif days == 80:
            assert solution == 5934
        else:
            assert solution == 26984457539
    else:
        assert solution == 1595779846729
