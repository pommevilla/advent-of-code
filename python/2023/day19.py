from ..aoc_utils import part_header, highlight
from ast import literal_eval
from collections import defaultdict
import re


def parse_rule(rule: str) -> tuple[str, str, int, str]:
    rule, dest = rule.split(":")
    parts = re.split("([^a-zA-Z])", rule, maxsplit=1)
    char, comp, value = parts[0], parts[1], parts[2]
    value = int(value)
    return (char, comp, value, dest)


def get_next_dest(parts_dictionary: dict[str, int], rules_list: list[str]) -> str:
    for rule in rules_list[:-1]:
        char, comp, value, dest = rule
        if comp == ">":
            if parts_dictionary[char] > value:
                return dest
        elif comp == "<":
            if parts_dictionary[char] < value:
                return dest

    return rules_list[-1]


def parse_workflows(raw_workflows: str) -> dict[str, list[str]]:
    d = {}
    for wf in raw_workflows.splitlines():
        wf_name, wf_rules = wf.split("{")
        wf_rules = wf_rules[:-1].split(",")
        d[wf_name] = [wf_rules.pop()]
        for rule in wf_rules:
            char, comp, value, dest = parse_rule(rule)
            d[wf_name].insert(-1, (char, comp, value, dest))
    return d


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    workflows, parts = open(input_file).read().split("\n\n")

    wf_dict = parse_workflows(workflows)

    parts = parts.split("\n")
    for i, part in enumerate(parts):
        part_dict: dict[str, int] = {}
        for ctg in part[1:-1].split(","):
            ctg, rating = ctg.split("=")
            part_dict[ctg] = int(rating)

        dest = "in"
        while dest not in ("A", "R"):
            dest = get_next_dest(part_dict, wf_dict[dest])

        if dest == "A":
            solution += sum(part_dict.values())

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 19114
    else:
        assert solution == 346230


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    workflows, _ = open(input_file).read().split("\n\n")
    wf_dict = parse_workflows(workflows)

    def count_valid_combinations(
        xmas_value_ranges: dict[str, tuple[int, int]], current_wf: str
    ):
        if current_wf == "R":
            return 0
        if current_wf == "A":
            count = 1
            # xmas_value_ranges is a dictionary whose values are a pair of integers representing
            # the range of valid values for that category we're checking.
            # If we're accepting it, then add the count of all of them to the total count
            for a, b in xmas_value_ranges.values():
                count *= b - a + 1
            return count

        rules_list = wf_dict[current_wf]

        total = 0

        for rule in rules_list[:-1]:
            char, comp, value, dest = rule
            a, b = xmas_value_ranges[char]

            # Construct the accept/reject ranges based on comparison
            if comp == ">":
                accepted_range = (max(value + 1, a), b)
                rejected_range = (a, min(value, b))
                # T = (max(n + 1, lo), hi)
                # F = (lo, min(n, hi))
            elif comp == "<":
                accepted_range = (a, min(value - 1, b))
                rejected_range = (max(value, a), b)
            else:
                print(f"Unknown comparison: {comp}")

            if accepted_range[0] <= accepted_range[1]:
                new_ranges = dict(xmas_value_ranges)
                new_ranges[char] = accepted_range
                total += count_valid_combinations(new_ranges, dest)

            if rejected_range[0] <= rejected_range[1]:
                xmas_value_ranges = dict(xmas_value_ranges)
                xmas_value_ranges[char] = rejected_range
            else:
                break

        total += count_valid_combinations(xmas_value_ranges, rules_list[-1])

        return total

    initial_ranges = {char: (1, 4000) for char in "xmas"}
    solution = count_valid_combinations(initial_ranges, "in")

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 167409079868000
    else:
        assert solution == 124693661917133
