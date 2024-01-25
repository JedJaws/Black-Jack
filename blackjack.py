#! /usr/bin/env python3
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


""" This is the file blackjack.py and it runs the whole program"""


from blackjackgame import game
from blackjackgame import __init__


if __name__ == "__main__":
    BLACKJACK = game.BlackJackGame()
    BLACKJACK.run()
