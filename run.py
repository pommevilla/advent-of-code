import argparse
import os
from datetime import datetime
from importlib import import_module


def run(func, filename="filename", testing: bool = True):
    func(filename, testing)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="Year of the challenge",
        default=datetime.now().year,
    )
    parser.add_argument(
        "-d", "--day", type=int, help="Day of the challenge", required=True
    )
    parser.add_argument("-t", "--test", action="store_true", help="Run the test input")
    args = parser.parse_args()

    input_file = (
        f"inputs/{args.year}/day{args.day}/{'sample' if args.test else 'input'}.txt"
    )

    print(
        f"Running day {args.day} from {args.year} on {'test' if args.test else 'real'} input\n"
    )

    # os.system(f"python -m {input_file} {test_flag}")
    module_name = f"python.{args.year}.day{args.day}"

    module = import_module(module_name)
    for i in [1, 2]:
        run(getattr(module, f"part_{i}"), input_file, args.test)
