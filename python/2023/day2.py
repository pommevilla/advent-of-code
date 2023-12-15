from ..aoc_utils import part_header


def game_iterator(line: str):
    game_data = line.split(":")[1].strip()
    for draw in game_data.split(";"):
        yield draw.strip()


def draw_iterator(draw: str):
    for num, color in draw.split(","):
        print("Huh")
        yield int(num), color


@part_header(part=1)
def part_1(input: str, test: bool = False):
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    sum = 0
    with open(input) as fin:
        for i, line in enumerate(fin):
            valid_game = True
            for draws in game_iterator(line):
                if not valid_game:
                    break
                for draw in draws.split(","):
                    num, color = draw.strip().split(" ")
                    if int(num) > cubes[color]:
                        valid_game = False
                        break

            if valid_game:
                sum += i + 1

    print(f"\nSolution: {sum}")

    if test:
        assert sum == 8
    else:
        assert sum == 2512


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    sum = 0
    with open(input_file) as fin:
        for line in fin:
            min_cube_colors = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for draws in game_iterator(line):
                for draw in draws.split(","):
                    num, color = draw.strip().split(" ")
                    num = int(num)
                    if num > min_cube_colors[color]:
                        min_cube_colors[color] = num
            sum += (
                min_cube_colors["red"]
                * min_cube_colors["green"]
                * min_cube_colors["blue"]
            )

    print(f"\nSolution: {sum}")

    if testing:
        assert sum == 2286
    else:
        assert sum == 67335
