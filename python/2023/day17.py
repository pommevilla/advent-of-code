from ..aoc_utils import part_header
from heapq import heappush, heappop
from time import sleep

dirs = {
    (0, 1): ">",
    (0, -1): "<",
    (1, 0): "v",
    (-1, 0): "^",
}


def print_grid(grid: list[list, int], path: set[tuple[int, int, int, int]]):
    out_string = ""
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            match = next(
                ((dx, dy) for vx, vy, dx, dy, in path if (x, y) == (vx, vy)), None
            )
            if match and match != (0, 0):
                out_string += f"\x1b[1;37;41m{dirs[match]}\x1b[0m "
            else:
                out_string += f"{str(char)} "
        out_string += "\n"
    print(out_string)


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    grid = [list(map(int, line.strip())) for line in open(input_file)]

    visited = set()
    # Heat loss, x, y, dx, dy, # steps in this direction
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        heat_loss, x, y, dx, dy, n_steps = heappop(pq)

        # If we're at the end, print heat loss
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            solution = heat_loss
            break

        # If we've already been to this node heading in the same direction
        # with the same number of steps, skip it
        if (x, y, dx, dy, n_steps) in visited:
            continue

        # Mark as visited
        visited.add((x, y, dx, dy, n_steps))

        # If we haven't moved in this direction three times and we're actually moving, move:
        if n_steps < 3 and (dx, dy) != (0, 0):
            # print(f"Moving from ({x}, {y}) to ({x + dx}, {y + dy})")
            new_x = x + dx
            new_y = y + dy
            # Add if we're in bounds
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                new_heat_loss = heat_loss + grid[new_x][new_y]
                heappush(pq, (new_heat_loss, new_x, new_y, dx, dy, n_steps + 1))

        # Check neighbors:
        for new_dx, new_dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Check if we're going backwards and if we're not going in the same direction
            # since we already took care of that case above
            if (new_dx, new_dy) != (-dx, -dy) and (new_dx, new_dy) != (dx, dy):
                new_x = x + new_dx
                new_y = y + new_dy
                # If in bounds, add to pq with new direction step counter
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    new_heat_loss = heat_loss + grid[new_x][new_y]
                    heappush(pq, (new_heat_loss, new_x, new_y, new_dx, new_dy, 1))

        # print_grid(grid, optimal_path)

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 102
    else:
        assert solution == 817


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    grid = [list(map(int, line.strip())) for line in open(input_file)]

    visited = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        heat_loss, x, y, dx, dy, n_steps = heappop(pq)

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            solution = heat_loss
            break

        if (x, y, dx, dy, n_steps) in visited:
            continue

        visited.add((x, y, dx, dy, n_steps))

        # If we haven't moved in this direction ten times and we're actually moving, move:
        if n_steps < 10 and (dx, dy) != (0, 0):
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                new_heat_loss = heat_loss + grid[new_x][new_y]
                heappush(pq, (new_heat_loss, new_x, new_y, dx, dy, n_steps + 1))

        # Same as part 1, but now we add an additional condition to check if we've moved
        # the minimum number of steps. If so, we handle that above.
        if n_steps >= 4 or (dx, dy) == (0, 0):
            for new_dx, new_dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (new_dx, new_dy) != (-dx, -dy) and (new_dx, new_dy) != (dx, dy):
                    new_x = x + new_dx
                    new_y = y + new_dy
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        new_heat_loss = heat_loss + grid[new_x][new_y]
                        heappush(pq, (new_heat_loss, new_x, new_y, new_dx, new_dy, 1))

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 94
    else:
        assert solution == 925
