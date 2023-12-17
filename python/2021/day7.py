from ..aoc_utils import part_header, highlight


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0
    crabs = list(map(int, open(input_file).read().split(",")))

    mean_pos = sum(crabs) // len(crabs)

    furthest_crab = max(crabs)
    best_position = 1e9

    lowest_fuel_cost = 1e9
    for i in range(furthest_crab):
        fuel_cost = sum([abs(i - crab) for crab in crabs])
        if fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost

    solution = lowest_fuel_cost

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 37
    else:
        assert solution == 356992


def calc_fuel_cost(pos: int, crab_pos: int) -> int:
    dist = abs(pos - crab_pos)
    return int(dist * (1 + dist) / 2)


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0
    crabs = list(map(int, open(input_file).read().split(",")))

    mean_pos = sum(crabs) // len(crabs)

    closest_crab = min(crabs)
    furthest_crab = max(crabs)

    lowest_fuel_cost = 1e9
    for i in range(closest_crab, furthest_crab):
        fuel_cost = sum([calc_fuel_cost(i, crab) for crab in crabs])
        if fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost

    solution = lowest_fuel_cost

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 168
    else:
        assert solution == 101268110
