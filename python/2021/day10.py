from ..aoc_utils import part_header, highlight, timer_func

open_close_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
p2_scores = {")": 1, "]": 2, "}": 3, ">": 4}


@part_header(part=1)
@timer_func
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = open(input_file).read().splitlines()

    for i, line in enumerate(lines):
        # print(f"{i} -> {line}")
        brackets_stack = []
        for j, char in enumerate(line):
            if char in open_close_pairs:
                brackets_stack.append(char)
            elif char == open_close_pairs[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                solution += scores[char]
                break

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 26397
    else:
        assert solution == 288291


@part_header(part=2)
@timer_func
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()

    scores = []
    for i, line in enumerate(lines):
        brackets_stack = []

        for j, char in enumerate(line):
            if char in open_close_pairs:
                brackets_stack.append(char)
            elif char == open_close_pairs[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                # If we find a corrupted line, stop processing and go to the next line
                break
        # If we finished processing the line, it isn't corrupted. Score it.
        else:
            score = 0
            brackets_stack = [open_close_pairs[x] for x in brackets_stack[::-1]]
            for char in brackets_stack:
                score = (5 * score) + p2_scores[char]
            scores.append(score)

    solution = sorted(scores)[len(scores) // 2]

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 288957
    else:
        assert solution == 820045242
