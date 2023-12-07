from enum import IntEnum
from functools import total_ordering

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

CardType = IntEnum("CardType", ["HIGH", "ONE", "TWO", "THREE", "FULL_HOUSE", "FOUR", "FIVE"])

@total_ordering
class Hand:
    card_values_map = {card: value for value, card in
                       enumerate(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))}

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        card_counts = {}
        for card in cards:
            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1
        counts = sorted(card_counts.values(), reverse=True)[:2]
        self.type = self._calc_type(counts)
        self.card_values = [self.card_values_map[card] for card in cards]

    def _calc_type(self, counts):
        counts = tuple(counts)
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
            return self.card_values < other.card_values
        else:
            return self.type < other.type

    def __eq__(self, other):
        return self.cards == other.cards and self.bid == other.bid


hands = [Hand(*line.split()) for line in lines]

silver = 0
for rank, hand in enumerate(sorted(hands)):
    silver += (rank + 1) * hand.bid

print("silver", silver)


class JokerHand(Hand):
    card_values_map = {card: value for value, card in
                       enumerate(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))}

    def __init__(self, cards, bid):
        super().__init__(cards, bid)
        joker_count = cards.count("J")
        cards_without_joker = cards.replace("J", "")
        card_counts = {}
        for card in cards_without_joker:
            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1
        counts = [5] if joker_count == 5 else sorted(card_counts.values(), reverse=True)[:2]
        counts[0] += joker_count
        self.type = self._calc_type(counts)


joker_hands = [JokerHand(*line.split()) for line in lines]
gold = 0
for rank, hand in enumerate(sorted(joker_hands)):
    gold += (rank + 1) * hand.bid

print("gold", gold)
