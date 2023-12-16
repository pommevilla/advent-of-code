from ..aoc_utils import part_header
from collections import deque
from time import sleep

dirs = {
    "D": (0, 1),
    "U": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

dir_chars = {
    "D": "V",
    "U": "^",
    "L": "<",
    "R": ">",
}

mirrors = {
    "\\": {
        "D": "R",
        "U": "L",
        "L": "U",
        "R": "D",
    },
    "/": {
        "D": "L",
        "U": "R",
        "L": "D",
        "R": "U",
    },
}


def in_bound(ray_pos: tuple[int, int], height: int, width=int) -> bool:
    return 0 <= ray_pos[0] < width and 0 <= ray_pos[1] < height


def move_ray(ray: tuple[int, int], direction: str) -> tuple[int, int]:
    return tuple(x + y for x, y in zip(ray, dirs[direction]))


def print_grid(
    grid: list[str],
    visited: set[tuple[int, int]],
    current_pos: tuple[int, int],
    direction: str,
    delay: float = 0.15,
):
    sleep(delay)
    out_string = ""
    for i, row in enumerate(grid):
        # print("\t", end="")
        out_string += "\t"
        for j, char in enumerate(row):
            if (j, i) == current_pos:
                pos_char = dir_chars[direction]
                # print(f"\x1b[1;37;41m{pos_char}\x1b[0m ", end="")
                out_string += f"\x1b[1;37;41m{pos_char}\x1b[0m "
            elif (j, i) in visited:
                out_string += "# "
                # print("# ", end="")
            else:
                out_string += f"{char} "
                # print(f"{char} ", end="")
        out_string += "\n"
        # print()
    print("".join(out_string))


def energize_tiles(
    grid: list[str],
    starting_position: tuple[int, int] = (0, 0),
    starting_dir: str = "R",
    print_out: bool = False,
) -> int:
    i = 0

    height = len(grid)
    width = len(grid[0])

    cache = set()
    visited = set()

    rays = deque()
    rays.append((starting_position, starting_dir))
    while rays:
        i += 1
        current_ray = rays.pop()
        pos, direction = current_ray

        # Check if we've already seen the ray
        # and if the current position is in bounds
        if current_ray in cache or not in_bound(pos, height, width):
            continue
        visited.add(pos)
        cache.add(current_ray)

        pos_char = grid[pos[1]][pos[0]]
        if pos_char == "|":
            if direction in ("L", "R"):
                new_pos = move_ray(pos, "U")
                rays.append((new_pos, "U"))
                new_pos = move_ray(pos, "D")
                rays.append((new_pos, "D"))
            else:
                new_pos = move_ray(pos, direction)
                rays.append((new_pos, direction))
        elif pos_char == "-":
            if direction in ("U", "D"):
                new_pos = move_ray(pos, "L")
                rays.append((new_pos, "L"))
                new_pos = move_ray(pos, "R")
                rays.append((new_pos, "R"))
            else:
                new_pos = move_ray(pos, direction)
                rays.append((new_pos, direction))
        elif pos_char in ("\\", "/"):
            new_dir = mirrors[pos_char][direction]
            new_pos = move_ray(pos, new_dir)
            rays.append((new_pos, new_dir))
        else:
            new_pos = move_ray(pos, direction)
            rays.append((new_pos, direction))
        if print_out:
            print(f"\n\n")
            print_grid(grid, visited, pos, direction)

    return len(visited)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    grid = open(input_file).read().splitlines()

    solution = energize_tiles(grid, print_out=testing)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 46
    else:
        assert solution == 8249


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    grid = open(input_file).read().splitlines()

    width = len(grid[0])
    height = len(grid)

    for i in range(width):
        solution = max(solution, energize_tiles(grid, (i, 0), "D"))
        solution = max(solution, energize_tiles(grid, (i, height - 1), "U"))
    for i in range(height):
        solution = max(solution, energize_tiles(grid, (0, i), "R"))
        solution = max(solution, energize_tiles(grid, (width - 1, i), "L"))

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 51
    else:
        assert solution == 8444
