from enum import IntEnum, Enum
from functools import total_ordering

# second.py contains both parts

with open("data.txt", "r") as f:
    lines = f.read().splitlines()


class CardType(IntEnum):
    HIGH = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FULL_HOUSE = 4
    FOUR = 5
    FIVE = 6

card_values_map = {card: value for value, card in
                   enumerate(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))}

@total_ordering
class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.card_counts = {}
        for card in cards:
            if card not in self.card_counts:
                self.card_counts[card] = 0
            self.card_counts[card] += 1
        self.type = self._calc_type()
        self.card_values = [card_values_map[card] for card in cards]
        print(self.cards, self.bid, self.card_counts, self.type, self.card_values)

    def _calc_type(self):
        counts = tuple(sorted(self.card_counts.values(), reverse=True)[:2])
        if counts == (5,):
            return CardType.FIVE
        elif counts == (4, 1):
            return CardType.FOUR
        elif counts == (3, 2):
            return CardType.FULL_HOUSE
        elif counts == (3, 1):
            return CardType.THREE
        elif counts == (2, 2):
            return CardType.TWO
        elif counts == (2, 1):
            return CardType.ONE
        else:
            return CardType.HIGH

    def __lt__(self, other):
        if self.type == other.type:
            for a, b in zip(self.card_values, other.card_values):
                if a < b:
                    return True
                elif b < a:
                    return False
            return False
        else:
            return self.type < other.type

    def __eq__(self, other):
        return self.cards == other.cards and self.bid == other.bid

hands = [Hand(*line.split()) for line in lines]

silver = 0
for rank, hand in enumerate(sorted(hands)):
    silver += (rank + 1) * hand.bid

print(silver)
