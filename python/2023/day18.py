from ..aoc_utils import part_header, highlight

dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


def move(pos: tuple[int, int], direction: str, steps: int) -> tuple[int, int]:
    x, y = pos
    dx, dy = dirs[direction]
    return (x + dx * steps, y + dy * steps)


def print_grid(
    border: dict[tuple[int, int], str],
    height: int,
    width: int,
    inside_points: set[tuple[int, int]],
):
    print()
    out_string = ""
    for i in range(height):
        out_string += f"{i:2d}\t"
        for j in range(width):
            if (i, j) in border:
                out_string += highlight("#", "yellow")
            elif (i, j) in inside_points:
                out_string += "X"
            else:
                out_string += "."
        out_string += "\n"
    print(out_string)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = open(input_file).read().splitlines()

    current_pos = (0, 0)
    border: dict[tuple[int, int], str] = {}
    vertices: list[int, int] = [(0, 0)]
    height = 0
    width = 0

    for i, line in enumerate(lines):
        dir_, steps, color = line.split()
        # print(f"\t{dir_} {steps} {color}")
        for _ in range(int(steps)):
            border[current_pos] = color
            current_pos = move(current_pos, dir_, 1)
        height = max(height, current_pos[0])
        width = max(width, current_pos[1])
        vertices.append(current_pos)
    # print(vertices)

    inside = set()

    this_height = height + 5
    this_width = width + 5

    # Ray tracing method
    # for i in range(this_height):
    #     crossing_count = 0
    #     current_pos = (i, 0)
    #     on_edge = False
    #     print(f"{i}\t{crossing_count=} -> ", end="")
    #     for j in range(this_width):
    #         last_pos = move(current_pos, "L", 1)

    #         if current_pos in border:
    #             if last_pos not in border:
    #                 if not on_edge:
    #                     on_edge = True
    #                     edge_start = j
    #         else:
    #             if on_edge:
    #                 on_edge = False
    #                 if edge_start == 0:
    #                     crossing_count += 2
    #                 else:
    #                     crossing_count += 1
    #             if crossing_count % 2 == 1:
    #                 inside.add(current_pos)
    #         current_pos = move(current_pos, "R", 1)

    # print(f"{crossing_count=}")

    # print_grid(border, this_height, this_width, inside)

    # Shoelace method to calculate area inside the polygon
    # Using the version in https://en.wikipedia.org/wiki/Shoelace_formula#Other_formulas
    shoelace = 0
    for i in range(len(vertices)):
        x0 = vertices[i][0]
        y_next = vertices[(i + 1) % len(vertices)][1]
        y_prev = vertices[i - 1][1]
        shoelace += x0 * (y_next - y_prev)
    shoelace = abs(shoelace) // 2

    # Pick's theorem
    # From here: https://en.wikipedia.org/wiki/Pick%27s_theorem#Formula
    inner_area = shoelace - len(border) // 2 + 1

    solution = inner_area + len(border)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 62
    else:
        assert solution == 53300


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()

    # To translate the last character in the direction string
    p2_dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}

    current_pos = (0, 0)

    # Since the input is much larger, we're not going to keep track of the
    # location of the borders, but only count how many there are.
    border: int = 0
    vertices: list[int, int] = [(0, 0)]

    for i, line in enumerate(lines):
        _, _, directions = line.split()
        directions = directions[2:-1]
        steps = int(directions[:-1], 16)
        dir_ = p2_dirs[directions[-1]]
        border += steps
        current_pos = move(current_pos, dir_, steps)
        vertices.append(current_pos)

    shoelace = 0
    for i in range(len(vertices)):
        x0 = vertices[i][0]
        y_next = vertices[(i + 1) % len(vertices)][1]
        y_prev = vertices[i - 1][1]
        shoelace += x0 * (y_next - y_prev)
    shoelace = abs(shoelace) // 2

    inner_area = shoelace - border // 2 + 1

    solution = inner_area + border

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 952408144115
    else:
        assert solution == 64294334780659
