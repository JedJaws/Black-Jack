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


""" This is the file game.py, it holds the essence of the gamee"""


import time


from .player import Player
from .player import Dealer
from .player import to_file
from .player import from_file
from .cards import Deck
from .cards import hand_value
from .cards import stringify_card


class BlackJackGame:

    """This is Black Jack or 21"""

    def __init__(self):
        self._is_game_not_over = True
        self._players = []

    @classmethod
    def pylint_passer(cls):
        "does nothing" ""

    def run(self):
        """Runs the game"""
        while self._is_game_not_over:
            intro_message = (
                "Good Evening Player(s)\n"
                "I will be your dealer, Francois McGillicuddy.\n"
                "This game will determine if you have what it takes\n"
                "to join the 21 club. It's all about counting cards\n"
                "and taking bank, best of luck ( '___' ).\n\n"
            )

            for i in intro_message:
                print(i, end="", flush=True)
                time.sleep(0.07)

            return_prompt = "Are you a returning player(s) [y/n]? "

            for i in return_prompt:
                print(i, end="", flush=True)
                time.sleep(0.07)

            return_ans = input("")

            if return_ans == "y":
                self._players = from_file("players.pckl")
            else:
                player_prompt = "How many players will be joining us [1 - 4]? "
                for i in player_prompt:
                    print(i, end="", flush=True)
                    time.sleep(0.07)

                num_players = int(input(""))

                follow_up = "You have entered {}\n\n".format(num_players)
                for i in follow_up:
                    print(i, end="", flush=True)
                    time.sleep(0.07)

                for i in range(num_players):
                    name_prompt = "What is your name patron {}? ".format(i + 1)
                    for j in name_prompt:
                        print(j, end="", flush=True)
                        time.sleep(0.07)
                    player_name = input("")
                    self._players.append(Player(player_name))

                self._players.append(Dealer(self))

            start_prompt = (
                "\nWell with formalities settled, let's begin!\n"
                "I will first start by shuffling and cutting the deck.\n\n"
            )

            for i in start_prompt:
                print(i, end="", flush=True)
                time.sleep(0.07)

            game_deck = Deck()
            for _ in range(7):
                game_deck.merge(Deck())

            for _ in range(2):
                game_deck.shuffle()

            game_deck.cut()

            current_index = 0
            dealer_sum = 0
            player_sum = 0
            while True:
                curr_pl = self._players[current_index]
                curr_pl = self._players[0]

                if curr_pl == self._players[0]:
                    play_prompt = (
                        "How do you do {}, would"
                        " everyone like to participate [y/"
                        "n]? ".format(curr_pl)
                    )

                    for i in play_prompt:
                        print(i, end="", flush=True)
                        time.sleep(0.07)

                    prompt_ans = input("")

                if prompt_ans == "y":
                    current_index = 0
                    while True:
                        curr_pl = self._players[current_index]
                        curr_pl.empty_hand()
                        curr_pl._score = 0
                        ins_check = 0

                        if curr_pl._name == "Francois McGillicuddy":
                            break

                        bank_amt = "Great! {}, you currently" " have ${}\n".format(
                            curr_pl, curr_pl._balance
                        )

                        for i in bank_amt:
                            print(i, end="", flush=True)
                            time.sleep(0.07)

                        print(curr_pl.will_bet())

                        amt_res = "You have wagered ${}\n\n".format(curr_pl._bet)

                        for i in amt_res:
                            print(i, end="", flush=True)
                            time.sleep(0.07)

                        current_index = (current_index + 1) % len(self._players)

                else:
                    bye_prompt = (
                        "It was an honor being you're dealer\n"
                        "Perhaps we will meet again.\n\n"
                    )

                    for i in bye_prompt:
                        print(i, end="", flush=True)
                        time.sleep(0.07)

                    to_file("players.pckl", self._players)

                    return 0

                play_len = len(self._players)
                play_len = play_len * 2
                single_card = game_deck.deal()
                j = 0
                for i in range(0, 2):
                    for j in self._players:
                        curr_pl = self._players[current_index]
                        curr_pl._hand[0].append(game_deck.deal())
                        current_index = (current_index + 1) % len(self._players)

                game_start = "Alright, cards have been dealt!\n\n"
                for i in game_start:
                    print(i, end="", flush=True)
                    time.sleep(0.07)

                current_index = 0
                hand_one = 0
                hand_two = 0
                ins_one = 0
                ins_two = 0
                while True:
                    curr_pl = self._players[current_index]
                    if curr_pl._name == "Francois McGillicuddy":
                        while dealer_sum < 17:
                            curr_pl._hand[0].append(game_deck.deal())
                            dealer_sum = dealer_sum + hand_value(
                                curr_pl._hand[0][len(curr_pl._hand[0]) - 1]
                            )

                        for play_run in self._players:

                            if play_run._name == "Francois McGillicuddy":
                                break

                            if play_run._hand[1]:
                                for curr_hand in range(0, 2):
                                    print(
                                        "{}, your hand is: ".format(play_run),
                                        (play_run._hand[curr_hand]),
                                        "\nThe Dealer" " hand is: ",
                                        self._players[len(self._players) - 1]._hand[0],
                                        "\n",
                                    )

                                    if curr_hand == 0:
                                        player_score = hand_one
                                    else:
                                        player_score = hand_two

                                    if curr_hand == 0:
                                        if ins_check == 21:
                                            if ins_one > 0:
                                                play_run._balance = (
                                                    play_run._balance + (ins_one * 2)
                                                )
                                                ins_win = (
                                                    "Good call on that insurance bet {}!\n"
                                                    "Your balance is now: ${}\n\n".format(
                                                        play_run._name,
                                                        play_run._balance,
                                                    )
                                                )
                                                for i in ins_win:
                                                    print(i, end="", flush=True)
                                                    time.sleep(0.07)
                                        else:
                                            if ins_one > 0:
                                                play_run._balance = (
                                                    play_run._balance - ins_one
                                                )
                                                ins_lose = (
                                                    "Bad call on that insurance bet {}!\n"
                                                    "Your balance is now: ${}\n\n".format(
                                                        play_run._name,
                                                        play_run._balance,
                                                    )
                                                )
                                                for j in ins_lose:
                                                    print(j, end="", flush=True)
                                                    time.sleep(0.07)
                                    else:
                                        if ins_check == 21:
                                            if ins_two > 0:
                                                play_run._balance = (
                                                    play_run._balance + (ins_two * 2)
                                                )
                                                ins_win = (
                                                    "Good call on that insurance bet {}!\n"
                                                    "Your balance is now: ${}\n\n".format(
                                                        play_run._name,
                                                        play_run._balance,
                                                    )
                                                )
                                                for i in ins_win:
                                                    print(i, end="", flush=True)
                                                    time.sleep(0.07)
                                        else:
                                            if ins_two > 0:
                                                play_run._balance = (
                                                    play_run._balance - ins_two
                                                )
                                                ins_lose = (
                                                    "Bad call on that insurance bet {}!\n"
                                                    "Your balance is now: ${}\n\n".format(
                                                        play_run._name,
                                                        play_run._balance,
                                                    )
                                                )
                                                for j in ins_lose:
                                                    print(j, end="", flush=True)
                                                    time.sleep(0.07)

                                    if player_score > 21:
                                        play_run._balance = (
                                            play_run._balance - play_run._bet
                                        )
                                        lose_prompt = (
                                            "Sorry about that bust {}.\n"
                                            "Your new balance: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in lose_prompt:
                                            print(i, end="", flush=True)
                                            time.sleep(0.09)
                                        curr_hand += 1
                                    elif dealer_sum > 21:
                                        play_run._balance = play_run._balance + (
                                            play_run._bet * 2
                                        )
                                        deal_bust = (
                                            "Nice hand {}! Winner Winner Chicken Dinner!\n"
                                            "I busted :(\n"
                                            "Your new balance: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in deal_bust:
                                            print(i, end="", flush=True)
                                            time.sleep(0.09)
                                        curr_hand += 1
                                    elif player_score > dealer_sum:
                                        play_run._balance = play_run._balance + (
                                            play_run._bet * 2
                                        )
                                        win_prompt = (
                                            "Nice hand {}! Winner Winner Chicken Dinner!\n"
                                            "Your new balance: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in win_prompt:
                                            print(i, end="", flush=True)
                                            time.sleep(0.09)
                                        curr_hand += 1
                                    elif player_score == dealer_sum:
                                        push_prompt = (
                                            "Your hand broke even {}!\n"
                                            "Your balance remains: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in push_prompt:
                                            print(i, end="", flush=True)
                                            time.sleep(0.09)
                                        curr_hand += 1
                                    else:
                                        play_run._balance = (
                                            play_run._balance - play_run._bet
                                        )
                                        lose_prompt = (
                                            "Sorry {}, your hand lost.\n"
                                            "Your new balance: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in lose_prompt:
                                            print(i, end="", flush=True)
                                            time.sleep(0.09)
                                        curr_hand += 1
                            else:
                                print(
                                    "{}, your hand is: ".format(play_run),
                                    (play_run._hand[0]),
                                    "\nThe Dealer" " hand is: ",
                                    self._players[len(self._players) - 1]._hand[0],
                                    "\n",
                                )

                                player_score = play_run._score

                                if ins_check == 21:
                                    if play_run._insurance > 0:
                                        play_run._balance = play_run._balance + (
                                            play_run._insurance * 2
                                        )
                                        ins_win = (
                                            "Good call on that insurance bet {}!\n"
                                            "Your balance is now: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for i in ins_win:
                                            print(i, end="", flush=True)
                                            time.sleep(0.07)
                                else:
                                    if play_run._insurance > 0:
                                        play_run._balance = (
                                            play_run._balance - play_run._insurance
                                        )
                                        ins_lose = (
                                            "Bad call on that insurance bet {}!\n"
                                            "Your balance is now: ${}\n\n".format(
                                                play_run._name, play_run._balance
                                            )
                                        )
                                        for j in ins_lose:
                                            print(j, end="", flush=True)
                                            time.sleep(0.07)

                                if player_score > 21:
                                    play_run._balance = (
                                        play_run._balance - play_run._bet
                                    )
                                    lose_prompt = (
                                        "Sorry about that bust {}.\n"
                                        "Your new balance: ${}\n\n".format(
                                            play_run._name, play_run._balance
                                        )
                                    )
                                    for i in lose_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.09)
                                elif dealer_sum > 21:
                                    play_run._balance = play_run._balance + (
                                        play_run._bet * 2
                                    )
                                    deal_bust = (
                                        "Nice hand {}! Winner Winner Chicken Dinner!\n"
                                        "I busted :(\n"
                                        "Your new balance: ${}\n\n".format(
                                            play_run._name, play_run._balance
                                        )
                                    )
                                    for i in deal_bust:
                                        print(i, end="", flush=True)
                                        time.sleep(0.09)
                                elif player_score > dealer_sum:
                                    play_run._balance = play_run._balance + (
                                        play_run._bet * 2
                                    )
                                    win_prompt = (
                                        "Nice hand {}! Winner Winner Chicken Dinner!\n"
                                        "Your new balance: ${}\n\n".format(
                                            play_run._name, play_run._balance
                                        )
                                    )
                                    for i in win_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.09)
                                elif player_score == dealer_sum:
                                    push_prompt = (
                                        "Your hand broke even {}!\n"
                                        "Your balance remains: ${}\n\n".format(
                                            play_run._name, play_run._balance
                                        )
                                    )
                                    for i in push_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.09)
                                else:
                                    play_run._balance = (
                                        play_run._balance - play_run._bet
                                    )
                                    lose_prompt = (
                                        "Sorry {}, your hand lost.\n"
                                        "Your new balance: ${}\n\n".format(
                                            play_run._name, play_run._balance
                                        )
                                    )
                                    for i in lose_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.09)

                        break

                    curr_pl._insurance = 0

                    print(
                        "{}, your hand is: ".format(curr_pl),
                        (curr_pl._hand[0][0][0]),
                        ", ",
                        (curr_pl._hand[0][1][0]),
                        "\nThe Dealer" " hand is: ",
                        (self._players[len(self._players) - 1]._hand[0][0][0]),
                        "\n",
                    )

                    player_sum = hand_value(curr_pl._hand[0][0]) + hand_value(
                        curr_pl._hand[0][1]
                    )
                    curr_pl._score = player_sum
                    dealer_sum = hand_value(
                        self._players[len(self._players) - 1]._hand[0][0]
                    ) + hand_value(self._players[len(self._players) - 1]._hand[0][1])
                    ins_check = dealer_sum

                    if hand_value(curr_pl._hand[0][0]) == hand_value(
                        curr_pl._hand[0][1]
                    ):

                        split_prompt = "Would you like to split [y/n]? "
                        for i in split_prompt:
                            print(i, end="", flush=True)
                            time.sleep(0.07)

                        split_ans = input("")

                        if split_ans == "y":
                            curr_pl._bet *= 2
                            split_prompt = (
                                "So you've decided to split ehhhh, that means"
                                " your bet is now {}\n\n".format(curr_pl._bet)
                            )
                            for i in split_prompt:
                                print(i, end="", flush=True)
                                time.sleep(0.07)

                            while True:
                                curr_pl._hand[1].append(curr_pl._hand[0][1])
                                curr_pl._hand[0].remove(curr_pl._hand[0][1])
                                curr_pl._hand[0].append(game_deck.deal())
                                curr_pl._hand[1].append(game_deck.deal())

                                print(
                                    "\n{}, you have two hands:\n".format(curr_pl),
                                    "First: ",
                                    curr_pl._hand[0],
                                    "\nSecond: ",
                                    curr_pl._hand[1],
                                    "\nThe Dealer hand is: ",
                                    self._players[len(self._players) - 1]._hand[0][0][
                                        0
                                    ],
                                    "\n" "\n",
                                )

                                hand_one = hand_value(curr_pl._hand[0][0]) + hand_value(
                                    curr_pl._hand[0][1]
                                )
                                hand_two = hand_value(curr_pl._hand[1][0]) + hand_value(
                                    curr_pl._hand[1][1]
                                )

                                curr_hand = 0
                                for i in range(0, 2):

                                    print("\nHand ", curr_hand + 1, ":")
                                    print(curr_pl._hand[i])
                                    print(
                                        "The Dealer hand is: ",
                                        self._players[len(self._players) - 1]._hand[0][
                                            0
                                        ][0],
                                        "\n\n",
                                    )
                                    print(curr_pl.will_doubledown())
                                    while True:
                                        if (
                                            hand_value(
                                                self._players[
                                                    len(self._players) - 1
                                                ]._hand[0][0]
                                            )
                                            == 10
                                            or hand_value(
                                                self._players[
                                                    len(self._players) - 1
                                                ]._hand[0][0]
                                            )
                                            == 11
                                        ):
                                            ins_prompt = "Would you like to purchase insurance [y/n]? "
                                            for i_p in ins_prompt:
                                                print(i_p, end="", flush=True)
                                                time.sleep(0.07)

                                            ins_ans = input("")

                                            if ins_ans == "y":
                                                bet_prompt = (
                                                    "How much would you like to bet? $"
                                                )
                                                for b_p in bet_prompt:
                                                    print(b_p, end="", flush=True)
                                                    time.sleep(0.07)

                                                if curr_hand == 0:
                                                    ins_one = int(input(""))
                                                else:
                                                    ins_two = int(input(""))
                                                print("\n")
                                                break
                                            else:
                                                break
                                        else:
                                            break

                                    if curr_hand == 1:
                                        while True:
                                            hit_prompt = "Would you like to hit [y/n]? "
                                            for h_p in hit_prompt:
                                                print(h_p, end="", flush=True)
                                                time.sleep(0.07)

                                            hit_ans = input("")

                                            if hit_ans == "y":
                                                curr_pl._hand[curr_hand].append(
                                                    game_deck.deal()
                                                )
                                                hand_two = hand_two + hand_value(
                                                    curr_pl._hand[1][
                                                        len(curr_pl._hand[curr_hand])
                                                        - 1
                                                    ]
                                                )
                                                after_hit = (
                                                    "\n{}, your current"
                                                    " hand is now: ".format(curr_pl),
                                                    (curr_pl._hand[curr_hand]),
                                                    "\n\n",
                                                )
                                                for a_h in after_hit:
                                                    print(a_h, end="", flush=True)
                                                    time.sleep(0.07)

                                                if hand_two > 21:
                                                    bust_prompt = (
                                                        "\nAHHH you fool!"
                                                        " you've busted\n"
                                                        "Better luck next"
                                                        " time ( '___' ).\n\n"
                                                    )
                                                    for b_p in bust_prompt:
                                                        print(b_p, end="", flush=True)
                                                        time.sleep(0.07)

                                                    break
                                            else:
                                                curr_hand += 1
                                                print("\n")
                                                break
                                    else:
                                        while True:
                                            hit_prompt = "Would you like to hit [y/n]? "
                                            for h_p in hit_prompt:
                                                print(h_p, end="", flush=True)
                                                time.sleep(0.07)

                                            hit_ans = input("")

                                            if hit_ans == "y":
                                                curr_pl._hand[curr_hand].append(
                                                    game_deck.deal()
                                                )
                                                hand_one = hand_one + hand_value(
                                                    curr_pl._hand[0][
                                                        len(curr_pl._hand[curr_hand])
                                                        - 1
                                                    ]
                                                )
                                                after_hit = (
                                                    "\n{}, your current"
                                                    " hand is now: ".format(curr_pl),
                                                    (curr_pl._hand[curr_hand]),
                                                    "\n\n",
                                                )
                                                for a_h in after_hit:
                                                    print(a_h, end="", flush=True)
                                                    time.sleep(0.07)

                                                if hand_one > 21:
                                                    bust_prompt = (
                                                        "\nAHHH you fool! "
                                                        "you've busted\n"
                                                        "Better luck next"
                                                        " time ( '___' ).\n\n"
                                                    )
                                                    for b_p in bust_prompt:
                                                        print(b_p, end="", flush=True)
                                                        time.sleep(0.07)

                                                    break
                                            else:
                                                curr_hand += 1
                                                print("\n")
                                                break
                                print("\n")
                                break
                            current_index = (current_index + 1) % len(self._players)
                    else:

                        print(curr_pl.will_doubledown())
                        while True:
                            if (
                                hand_value(
                                    self._players[len(self._players) - 1]._hand[0][0]
                                )
                                == 10
                                or hand_value(
                                    self._players[len(self._players) - 1]._hand[0][0]
                                )
                                == 11
                            ):
                                ins_prompt = (
                                    "Would you like to " "purchase insurance [y/n]? "
                                )
                                for i in ins_prompt:
                                    print(i, end="", flush=True)
                                    time.sleep(0.07)

                                ins_ans = input("")

                                if ins_ans == "y":
                                    bet_prompt = "How much would you like to bet? $"
                                    for i in bet_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.07)

                                    curr_pl._insurance = int(input(""))
                                    print("\n")
                                    break
                                else:
                                    break
                            else:
                                break

                        while True:
                            hit_prompt = "Would you like to hit [y/n]? "
                            for i in hit_prompt:
                                print(i, end="", flush=True)
                                time.sleep(0.07)

                            hit_ans = input("")

                            if hit_ans == "y":
                                curr_pl._hand[0].append(game_deck.deal())
                                player_sum = player_sum + hand_value(
                                    curr_pl._hand[0][len(curr_pl._hand[0]) - 1]
                                )
                                curr_pl._score = player_sum
                                after_hit = (
                                    "\n{}, your current hand is now: ".format(curr_pl),
                                    (curr_pl._hand[0]),
                                )
                                for i in after_hit:
                                    print(i, end="", flush=True)
                                    time.sleep(0.07)

                                if player_sum > 21:
                                    bust_prompt = (
                                        "\nAHHH you fool! you've busted\n"
                                        "Better luck next time ( '___' ).\n\n"
                                    )

                                    for i in bust_prompt:
                                        print(i, end="", flush=True)
                                        time.sleep(0.07)

                                    break

                            else:
                                print("\n")
                                break

                        current_index = (current_index + 1) % len(self._players)
