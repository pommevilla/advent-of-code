import argparse
from ..aoc_utils import part_header

sample_input = "inputs/day5/sample.txt"
real_input = "inputs/day5/input.txt"


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    smallest_destination = 1e10

    with open(input_file) as fin:
        seeds = [int(x) for x in fin.readline().split(":")[1].split()]

        all_maps = fin.read().split("\n\n")
        all_maps = [x.split(":")[1] for x in all_maps]
        all_maps = [x.strip().split("\n") for x in all_maps]
        all_maps = [[[int(x) for x in il.split()] for il in l] for l in all_maps]

        for seed in seeds:
            step = seed
            for maps in all_maps:
                found = False
                for map in maps:
                    if found:
                        continue
                    if map[1] <= step <= map[1] + map[2]:
                        step = map[0] + (step - map[1])
                        found = True
                        continue

            if step < smallest_destination:
                smallest_destination = step

    print(f"\n\tSolution: {smallest_destination}")

    if testing:
        assert smallest_destination == 35
    else:
        assert smallest_destination == 457535844


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    with open(input_file) as fin:
        ranges = [int(x) for x in fin.readline().split(":")[1].split()]

        seeds = []

        for r in range(0, len(ranges), 2):
            seeds.append((ranges[r], ranges[r] + ranges[r + 1]))

        all_maps = fin.read().split("\n\n")
        all_maps = [x.split(":")[1] for x in all_maps]
        all_maps = [x.strip().split("\n") for x in all_maps]
        all_maps = [[[int(x) for x in il.split()] for il in l] for l in all_maps]

        for maps in all_maps:
            new = []
            while seeds:
                start, end = seeds.pop()
                for a, b, c in maps:
                    other_start = max(start, b)
                    other_end = min(end, b + c)
                    if other_start < other_end:
                        new.append((other_start - b + a, other_end - b + a))
                        if other_start > start:
                            seeds.append((start, other_start))
                        if end > other_end:
                            seeds.append((other_end, end))
                        break
                else:
                    new.append((start, end))
            seeds = new

    print(min(seeds))
    smallest_destination = min(seeds)[0]

    print(f"\n\tSolution: {smallest_destination}")

    if testing:
        assert smallest_destination == 46
    # else:
    #     assert smallest_destination == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    part_1(input_file, args.test)
    part_2(input_file, args.test)
