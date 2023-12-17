from ..aoc_utils import part_header, highlight
import itertools


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = [
        [pair for pair in line.split(" | ")]
        for line in open(input_file).read().splitlines()
    ]

    for i, (signal_pattern, output_values) in enumerate(lines):
        for ov in output_values.split():
            if len(ov) in [2, 3, 4, 7]:
                solution += 1

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 26
    else:
        assert solution == 440


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = [
        [(pair) for pair in line.split(" | ")]
        for line in open(input_file).read().splitlines()
    ]

    letters = "abcdefg"
    number_wires = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]

    for i, (signal_pattern, output_values) in enumerate(lines):
        for perm in itertools.permutations(letters):
            wire_map = {new: old for new, old in zip(perm, letters)}
            translations = set()
            for signal in signal_pattern.split():
                translated_signal = "".join(sorted(map(wire_map.get, signal)))
                translations.add(translated_signal)
            if translations == set(number_wires):
                digits = output_values.split()
                out_digits = []
                for digit in digits:
                    translated_digit = "".join(sorted(map(wire_map.get, digit)))
                    translated_digit = "".join(
                        str(number_wires.index(translated_digit))
                    )
                    out_digits.append(translated_digit)

                translated_digit = int("".join(out_digits))

                solution += translated_digit
                break

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 61229
    else:
        assert solution == 1046281
