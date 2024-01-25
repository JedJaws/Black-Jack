# Christian Verry
# CPSC 386-03
# 2022-03-17
# CJVerry@csu.fullerton.edu
# @JedJaws
#
# Lab 03-00
#
# This module is my very first game!
#


""" This is the file cards.py, it holds the object of cards and its actions"""

from collections import namedtuple
from random import shuffle, randrange
from math import ceil

Card = namedtuple("Card", ["rank", "suit"])


def stringify_card(card_type):
    """convert a card to a nicely formatted string"""
    return f"{card_type.rank} of {card_type.suit}"


Card.__str__ = stringify_card


class Deck:
    """Deck classes"""

    rank = ["Ace"] + list(map(str, range(2, 11))) + "Jack Queen King".split()
    suit = "Clubs Hearts Spades Diamonds".split()
    values = list(range(1, 11)) + [10, 10, 10]
    value_dict = dict(zip(rank, values))

    def __init__(self):
        """Create one whole deck of cards."""
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.rank]

    def __str__(self):
        """joins cards"""
        return "\n".join(["{} {}".format(i, j) for i, j in enumerate(self._cards)])

    def __getitem__(self, position):
        """Return the card at the given position"""
        return self._cards[position]

    def shuffle(self, num_card=1):
        """shuffles the deck n times, default is 1"""
        for _ in range(num_card):
            shuffle(self._cards)

    def cut(self):
        """Cut the deck."""
        extra = ceil(len(self._cards) * 0.2)
        half = (len(self._cards) // 2) + randrange(-extra, extra)
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf

    def merge(self, the_other_deck):
        """merges the deck of cards together"""
        self._cards = self._cards + the_other_deck._cards

    def deal(self, num_card=1):
        """deals a single card to a player"""
        return [self._cards.pop() for i in range(num_card)]

    def __len__(self):
        """returns the length"""
        return len(self._cards)


def card_value(c_val):
    """Return the numerical value of the rank of a given card."""
    return Deck.value_dict[c_val.rank]


def hand_value(h_v):
    """Returns hand value"""
    hand_sum = sum(map(int, h_v))
    if sum(map(lambda c: c.rank == "Ace", h_v)) and hand_sum + 10 <= 21:
        hand_sum += 10
    return hand_sum


Card.value = card_value
Card.__int__ = card_value
