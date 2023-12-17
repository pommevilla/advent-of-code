import argparse
from datetime import datetime
import os
from pathlib import Path
import shutil

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

    args = parser.parse_args()

    print(f"Prepping day {args.day} from {args.year}")

    # Create inputs/year/dayX/input.txt and inputs/year/dayX/sample.txt
    os.makedirs(f"inputs/{args.year}/day{args.day}", exist_ok=True)
    Path(f"inputs/{args.year}/day{args.day}/input.txt").touch()
    Path(f"inputs/{args.year}/day{args.day}/sample.txt").touch()

    # Create python/year/dayX.py
    if not os.path.exists(f"python/{args.year}"):
        os.makedirs(f"python/{args.year}")

    # Copy python/template to python/year/dayX.py
    template_file = "python/template.py"
    new_file = f"python/{args.year}/day{args.day}.py"
    shutil.copyfile(template_file, new_file)
