from ..aoc_utils import part_header, highlight, timer_func


def print_dots(dots: list[tuple[int, int]], scale: int = 1, part2: bool = False):
    if part2:
        width = 100
        height = 8
    else:
        height = int(max(dots, key=lambda x: x[1])[1] * scale)
        width = int(max(dots, key=lambda x: x[0])[0] * scale)
    out_str = "\n"
    for i in range(height):
        out_str += f""
        for j in range(width):
            if (i, j) in dots:
                char = "#"
            else:
                char = " "
            out_str += f"{char}"
        out_str += "\n"
    print(out_str)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    dots, folds = open(input_file).read().split("\n\n")

    dots = [tuple(map(int, dot.split(","))) for dot in dots.split("\n")]

    if testing:
        print_dots(dots, scale=1.2)
    folds = [fold.split()[-1].split("=") for fold in folds.split("\n")]
    # print(folds)

    fold_dir = folds[0][0]
    fold_loc = int(folds[0][1])

    if fold_dir == "x":
        dots = {(x if x < fold_loc else fold_loc - (x - fold_loc), y) for x, y in dots}
    elif fold_dir == "y":
        dots = {(x, y if y < fold_loc else fold_loc - (y - fold_loc)) for x, y in dots}
    else:
        raise ValueError(f"Invalid fold direction: {fold_dir}")

    solution = len(dots)
    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 17
    else:
        assert solution == 664


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    dots, folds = open(input_file).read().split("\n\n")

    dots = [tuple(map(int, dot.split(","))) for dot in dots.split("\n")]

    folds = [fold.split()[-1].split("=") for fold in folds.split("\n")]

    for fold in folds:
        fold_dir = fold[0]
        fold_loc = int(fold[1])

        if fold_dir == "x":
            dots = {
                (x if x < fold_loc else fold_loc - (x - fold_loc), y) for x, y in dots
            }
        elif fold_dir == "y":
            dots = {
                (x, y if y < fold_loc else fold_loc - (y - fold_loc)) for x, y in dots
            }
        else:
            raise ValueError(f"Invalid fold direction: {fold_dir}")

    print_dots([(y, x) for x, y in dots], part2=True)

    # No testing on this one
    # if testing:
    #     assert solution == 17
    # else:
    #     assert solution == 664
