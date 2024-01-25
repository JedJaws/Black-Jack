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


""" This is the file player.py, it holds the object of players and dealers"""


import time
import pickle
from .cards import Deck


class Player:
    """This class creates the players and their actions"""

    def __init__(self, name, bankroll=10000):
        """Includes what makes a player"""
        self._name = name
        self._balance = bankroll
        self._hand = [[], []]
        self._bet = 0
        self._score = 0
        self._score1 = 0
        self._insurance = 0

    @property
    def name(self):
        """name for player"""
        return self._name

    def empty_hand(self):
        """Empties the hand of the player"""
        self._hand = [[], []]
        self._bet = 0
        
    def will_hit(self):
        """Deals a card to player"""
        

    def will_bet(self):
        """Asks player how mych they will bet"""
        bet_prompt = "How much will you bet? $"
        for i in bet_prompt:
            print(i, end="", flush=True)
            time.sleep(0.07)

        self._bet = int(input(""))
        return True

    def will_doubledown(self):
        """Asks player if they will double down"""
        answer = input("Do you want to D.D [y/n]? ")
        val = answer.lower() == "y"
        if val:
            self._bet *= 2
        return val

    def __str__(self):
        """type for name"""
        return self._name


class Dealer(Player):

    """The Dealer class"""

    def __init__(self, game, bankroll=(2 ** 32 - 1)):
        """Dealer is of player class"""
        super().__init__("Francois McGillicuddy")
        self._balance = bankroll
        self._game = game

    def will_bet(self):
        """Asks player how much they will bet"""
        self._bet = "How much will you bet? $"
        self._bet = 0
        return True

    def will_doubledown(self):
        """Asks player if they will double down"""
        print("Do you want to D.D[y/n]")
        val = "n"
        return val


def to_file(pickle_file, players):
    """Write the list players tot he file pickle_file."""
    with open(pickle_file, "wb") as file_handle:
        pickle.dump(players, file_handle, pickle.HIGHEST_PROTOCOL)


def from_file(pickle_file):
    """Read the contents of pickle_file, decode it, and return it as players"""
    with open(pickle_file, "rb") as file_handle:
        players = pickle.load(file_handle)
    return players
