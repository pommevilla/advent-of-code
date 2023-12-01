import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--day", type=int, help="Day of the challenge", required=True
    )
    parser.add_argument("-t", "--test", action="store_true", help="Run the test input")
    args = parser.parse_args()

    input_file = f"python/day{args.day}.py"

    test_flag = "-t" if args.test else ""

    print(f"Running day 1 on {'test' if args.test else 'real'} input\n")

    os.system(f"python {input_file} {test_flag}")
