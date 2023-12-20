from ..aoc_utils import part_header, highlight

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def print_octopi(octopi: list[list[int]]):
    out_str = "\n"
    for i, row in enumerate(octopi):
        out_str += f"\t{i}\t"
        for j, char in enumerate(row):
            if char == 0:
                char = highlight(char, "yellow")
            out_str += f"{char} "
        out_str += "\n"
    print(out_str)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    lines = open(input_file).read().splitlines()

    octopi = [list(map(int, line)) for line in lines]

    def increment_neighbors(i, j):
        total_flashes = 0
        for adj in adjacents:
            new_i = i + adj[0]
            new_j = j + adj[1]
            if 0 <= new_i < len(octopi) and 0 <= new_j < len(octopi[0]):
                octopi[new_i][new_j] += 1
                if octopi[new_i][new_j] == 10:
                    total_flashes += 1
                    total_flashes += increment_neighbors(new_i, new_j)
        return total_flashes

    num_steps = 100
    current_step = 0
    while current_step < num_steps:
        flashes = 0
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                octopi[i][j] += 1
                if octopi[i][j] == 10:
                    flashes += 1
                    flashes += increment_neighbors(i, j)
        current_step += 1

        # flashes = sum(1 for row in octopi for x in row if x > 9)
        # octopi = [[0 if x > 9 else x for x in row] for row in octopi]

        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopi[i][j] > 9:
                    octopi[i][j] = 0
        solution += flashes
        if current_step % 10 == 0 and testing:
            print(f"\t====== Step {current_step} ======")
            print_octopi(octopi)

    if testing:
        print(f"\t====== Final ======")
        print_octopi(octopi)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 1656
    else:
        assert solution == 1719


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    lines = open(input_file).read().splitlines()

    octopi = [list(map(int, line)) for line in lines]

    def increment_neighbors(i, j):
        total_flashes = 0
        for adj in adjacents:
            new_i = i + adj[0]
            new_j = j + adj[1]
            if 0 <= new_i < len(octopi) and 0 <= new_j < len(octopi[0]):
                octopi[new_i][new_j] += 1
                if octopi[new_i][new_j] == 10:
                    total_flashes += 1
                    total_flashes += increment_neighbors(new_i, new_j)
        return total_flashes

    num_steps = 500
    current_step = 0
    while current_step < num_steps:
        flashes = 0
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                octopi[i][j] += 1
                if octopi[i][j] == 10:
                    flashes += 1
                    flashes += increment_neighbors(i, j)
        current_step += 1

        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopi[i][j] > 9:
                    octopi[i][j] = 0
        if sum(sum(row) for row in octopi) == 0:
            break

    solution = current_step

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 195
    else:
        assert solution == 232
