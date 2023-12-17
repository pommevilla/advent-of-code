from ..aoc_utils import part_header, highlight


def is_horizontal_or_vertical(line: list[tuple[int, int]]):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def print_map(height: int, width: int, counts: dict[tuple[int, int], int]):
    out_str = ""
    print("\t\t", end="")
    for i in range(width):
        print(f"{i:2} ", end="")
    print()
    for y in range(height):
        out_str += f"\t{y:}\t"
        for x in range(width):
            current_char = counts.get((x, y), 0)
            if current_char >= 2:
                current_char = highlight(current_char, "red", padding=2)
            elif current_char == 0:
                current_char = " ."
            out_str += f"{current_char:2} "
        out_str += "\n"
    print(out_str)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = open(input_file).read().splitlines()
    lines = [
        [tuple(map(int, t.split(","))) for t in line.split(" -> ")] for line in lines
    ]
    lines = [line for line in lines if is_horizontal_or_vertical(line)]

    height = max(point[0] for line in lines for point in line) + 1
    width = max(point[1] for line in lines for point in line)

    counts: dict[tuple[int, int], int] = {}
    for (x1, y1), (x2, y2) in lines:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                counts[(x, y)] = counts.get((x, y), 0) + 1

    solution = len([k for k, v in counts.items() if v >= 2])

    if testing:
        print_map(height, width, counts)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 5
    else:
        assert solution == 7380


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()
    lines = [
        [tuple(map(int, t.split(","))) for t in line.split(" -> ")] for line in lines
    ]

    height = max(point[0] for line in lines for point in line) + 1
    width = max(point[1] for line in lines for point in line)

    counts: dict[tuple[int, int], int] = {}

    for (x1, y1), (x2, y2) in lines:
        print(f"From {(x1, y1)} to {(x2, y2)}")
        if is_horizontal_or_vertical(((x1, y1), (x2, y2))):
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    counts[(x, y)] = counts.get((x, y), 0) + 1
        else:
            step_x = 1 if x1 < x2 else -1
            step_y = 1 if y1 < y2 else -1
            for x, y in zip(
                range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)
            ):
                counts[(x, y)] = counts.get((x, y), 0) + 1
        if testing:
            print_map(height, width, counts)

    solution = len([k for k, v in counts.items() if v >= 2])

    if testing:
        print_map(height, width, counts)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 12
    else:
        assert solution == 7380
