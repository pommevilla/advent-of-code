import argparse
from aoc_utils import part_header
from collections import Counter, OrderedDict

sample_input = "inputs/day7/sample.txt"
real_input = "inputs/day7/input.txt"


class Hand:
    def __init__(self, hand: str, jokers: bool = False):
        self.hand = hand
        self.hand_counts = Counter(self.hand)
        self.jokers = jokers

    def __gt__(self, other):
        these_card_counts = self.get_card_counts()
        other_card_counts = other.get_card_counts()
        # print(f"\t{these_card_counts=} vs {other_card_counts=}")
        if these_card_counts[0][1] > other_card_counts[0][1]:
            return True
        elif these_card_counts[0][1] < other_card_counts[0][1]:
            return False
        else:
            if these_card_counts[0][1] == 3:
                if these_card_counts[1][1] == 2 and other_card_counts[1][1] == 1:
                    return True
                elif these_card_counts[1][1] == 1 and other_card_counts[1][1] == 2:
                    return False
                else:
                    return self.tiebreaker(other)
            elif these_card_counts[0][1] == 2:
                if these_card_counts[1][1] == 2 and other_card_counts[1][1] == 1:
                    return True
                elif these_card_counts[1][1] == 1 and other_card_counts[1][1] == 2:
                    return False
                else:
                    return self.tiebreaker(other)
            else:
                return self.tiebreaker(other)

    def get_card_counts(self):
        if self.jokers:
            joker_counts = self.hand_counts["J"]
            if 0 < joker_counts < 5:
                new_hand = self.hand_counts.copy()
                del new_hand["J"]
                new_hand[max(new_hand, key=new_hand.get)] += joker_counts
                return new_hand.most_common()
            else:
                return self.hand_counts.most_common()
        else:
            return self.hand_counts.most_common()

    def tiebreaker(self, other):
        for card in zip(self.hand, other.hand):
            if card_ranks.index(card[0]) > card_ranks.index(card[1]):
                return True
            elif card_ranks.index(card[0]) < card_ranks.index(card[1]):
                return False

    def __repr__(self):
        return f"Hand({self.hand})"


def read_hand_bids(input_file: str, jokers: bool = False) -> OrderedDict[Hand, int]:
    hand_bids = open(input_file).read().split("\n")

    hand_bids = OrderedDict(
        sorted(
            {
                Hand(hand_bid.split()[0], jokers=jokers): int(hand_bid.split()[1])
                for hand_bid in hand_bids
            }.items()
        )
    )

    return hand_bids


@part_header(part=1)
def part_1(input_file: str, testing: bool = False):
    solution = 0

    hand_bids = read_hand_bids(input_file)

    for i, (k, v) in enumerate(hand_bids.items(), 1):
        # print(f"\t{i}: {k.hand=}, {v=}")
        solution += v * i

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 6592
    else:
        assert solution == 251806792


@part_header(part=2)
def part_2(input_file: str, testing: bool):
    solution = 0

    hand_bids = read_hand_bids(input_file, jokers=True)

    for i, (k, v) in enumerate(hand_bids.items(), 1):
        # print(f"\t{i}: {k.hand=}, {v=}")
        solution += v * i

    print(f"\n\tSolution: {solution}")

    if testing:
        assert solution == 6839
    else:
        assert solution == 252113488


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="Whether or not to use the test input"
    )
    args = parser.parse_args()

    input_file = sample_input if args.test else real_input

    cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
    card_ranks = [card for card in cards.split(", ")][::-1]
    part_1(input_file, args.test)

    cards = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
    card_ranks = [card for card in cards.split(", ")][::-1]
    part_2(input_file, args.test)
