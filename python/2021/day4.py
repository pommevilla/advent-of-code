from ..aoc_utils import part_header, highlight
import copy


def print_board(board: list[list[int]]):
    out_str = ""
    for i, row in enumerate(board):
        out_str += f"   {i:2} "
        for col in row:
            out_str += f"{col:2} "
        out_str += "\n"
    print(out_str)


def print_boards(
    boards_list: list[list[list[int]]], called_numbers: set[int], num_boards=5
):
    num_boards = len(boards_list[0]) if num_boards > len(boards_list[0]) else num_boards

    out_strings = ["" for _ in range(num_boards)]
    print()

    for row in range(num_boards):
        out_strings[row] += "\t"
        for board in boards_list[:num_boards]:
            for num in board[row]:
                if num in called_numbers:
                    # num = f"\x1b[4;30;46m{num:2}\x1b[0m"
                    num = highlight(num, "blue", padding=2)
                out_strings[row] += f"{num:2} "
            out_strings[row] += "\t\t"
    print("\n".join(out_strings) + "\n")


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    with open(input_file) as fin:
        numbers = [int(x) for x in fin.readline().strip().split(",")]
        boards = [
            [[int(i) for i in l.split()] for l in x.splitlines()]
            for x in fin.read().strip().split("\n\n")
        ]

    viz_boards = copy.deepcopy(boards)

    called_numbers = set()

    # Change to break on winning
    winner_found = False
    for num in numbers:
        called_numbers.add(num)
        if winner_found:
            break
        print(
            f"\t\t\t======================== New number: {num} ========================"
        )
        print_boards(viz_boards, called_numbers)
        # Go through each board and remove all matches
        for board_num, board in enumerate(boards):
            for row in board:
                for i in range(len(row)):
                    if row[i] == num:
                        row[i] = None

            # Check if any row is a winner
            for i, row in enumerate(board):
                if all(x == None for x in row):
                    print(f"Winner found on board {board_num}, row {i}")
                    winner_found = True
                    break

            # Check if any column is a winner
            for j, col in enumerate(zip(*board)):
                if all(x == None for x in col):
                    print(f"Winner found on board {board_num}, column {j}")
                    winner_found = True
                    break

            if winner_found:
                solution = sum(x or 0 for row in board for x in row) * num
                break

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 4512
    else:
        assert solution == 63552


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    with open(input_file) as fin:
        numbers = [int(x) for x in fin.readline().strip().split(",")]
        boards = [
            [[int(i) for i in l.split()] for l in x.splitlines()]
            for x in fin.read().strip().split("\n\n")
        ]

    viz_boards = copy.deepcopy(boards)
    total_boards = len(boards)

    called_numbers = set()

    # Change to break on winning
    remaining_boards = total_boards
    winner_found = False
    # while remaining_boards > 1:
    #     print(f"{remaining_boards=}")
    for num in numbers:
        called_numbers.add(num)
        print(
            f"\t\t\t======================== New number: {num} ========================"
        )
        print_boards(viz_boards, called_numbers)
        inner_i = 0
        while inner_i < len(boards):
            current_board = boards[inner_i]
            for row in current_board:
                for i in range(len(row)):
                    if row[i] == num:
                        row[i] = None

            if any(all(x == None for x in row) for row in current_board) or any(
                all(x == None for x in col) for col in zip(*current_board)
            ):
                # print(f"Winner found on board {current_board}")
                remaining_boards -= 1
                last_board = boards[inner_i]
                del boards[inner_i]
                del viz_boards[inner_i]
            else:
                inner_i += 1

        if len(boards) == 0:
            break

    solution = sum(x or 0 for row in last_board for x in row) * num

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 1924
    else:
        assert solution == 9020
