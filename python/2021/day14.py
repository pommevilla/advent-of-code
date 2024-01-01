from ..aoc_utils import part_header, highlight, timer_func
from collections import Counter


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    polymer, pair_inserts = open(input_file).read().split("\n\n")
    pair_inserts = pair_inserts.split("\n")

    print(f"Polymer: {polymer}")
    pi_map = {}

    for pi in pair_inserts:
        pi_match, pi_insert = pi.split(" -> ")
        pi_map[pi_match] = pi_insert

    total_steps = 10
    current_step = 0

    while current_step < total_steps:
        print(current_step)
        new_polymer = ""
        for a, b in zip(polymer, polymer[1:]):
            poly_pair = a + b
            new_polymer += a + pi_map[poly_pair]
        new_polymer += b
        current_step += 1
        polymer = new_polymer

    poly_counts = Counter(polymer).most_common()
    solution = poly_counts[0][1] - poly_counts[-1][1]

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 1588
    else:
        assert solution == 3048


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    polymer, pair_inserts = open(input_file).read().split("\n\n")
    pair_inserts = pair_inserts.split("\n")

    print(f"Polymer: {polymer}")
    pi_map = {}

    for pi in pair_inserts:
        pi_match, pi_insert = pi.split(" -> ")
        pi_map[pi_match] = pi_insert

    total_steps = 40
    current_step = 0

    while current_step < total_steps:
        print(current_step)
        new_polymer = ""
        for a, b in zip(polymer, polymer[1:]):
            poly_pair = a + b
            new_polymer += a + pi_map[poly_pair]
        new_polymer += b
        current_step += 1
        polymer = new_polymer

    poly_counts = Counter(polymer).most_common()
    solution = poly_counts[0][1] - poly_counts[-1][1]

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 2188189693529
    else:
        assert solution == 3048
