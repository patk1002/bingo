#! /usr/env python
"""
This is to play bingo
Some ideas came from https://stackoverflow.com/questions/69601220/bingo-using-python
"""

import numpy as np
import random

letters = ["B", "I", "N", "G", "O"]

# random_draw_list = random.sample(range(1, 76), 75)

# def generate_card():
#     card = {
#         "B": [],
#         "I": [],
#         "N": [],
#         "G": [],
#         "O": [],
#     }
#     min = 1
#     max = 15
#     for letter in card:
#         card[letter] = random.sample(range(min, max), 5)
#         min += 15
#         max += 15
#         if letter == "N":
#             card[letter][2] = "X" # free space!
#     return card

# def IsBingo(card):
#     for i in range (5):
#         row_zeros=np.count_nonzero(card[i:,])
#         col_zeros=np.count_nonzero(card[:,i])
#         if not row_zeros or not col_zeros: #check if we have 0 non-zeros
#             return (True)
#     diagonal_zeros=np.count_nonzero(np.diag(card))
#     diagonal1_zeros=np.count_nonzero(np.diag(np.fliplr(card)))
#     if not diagonal_zeros or not diagonal1_zeros:
#         return(True)
#     return(False)

# # this will replace number in our card with zero if it matches
# card = np.where(card == number_that_we_check, 0, card) 

def generate_card():
    """
    Generate the Bingo card
    """
    print("Now the Bingo card is being generated.")
    card = np.array(([1, 2, 3, 4, 5],
                        [16, 17, 18, 19, 20],
                        [31, 32, 33, 34, 35],
                        [46, 47, 48, 49, 50],
                        [61, 62, 63, 64, 65]))
    return card


def print_card(card):
    """
    Print the Bingo card
    """
    print("Now printing the card as it is.")
    # print title letters first
    for index in range(5):
        print(letters[index], end="\t")
    print("")
    # print Bingo card
    for index in range(5):
        for index2 in range(5):
            print(card[index2][index], end="\t")
        print("")
    print("\n")


def play_bingo_game():
    """
    Play one Bingo game here
    """
    print("\nLet's play Bingo now...")
    card = generate_card()
    print("\nHere is your card:\n")
    print_card(card)
    print("Now you can enter the Bingo number, play, check for Bingo, and loop.")


def play_bingo_games():
    """
    Play multiple Bingo games, asking after each to continue or not
    """
    playAgain = True
    while (playAgain):
        play_bingo_game()
        playAgainInput = input("Do you want to play Bingo again? (y or n)")
        if playAgainInput.lower()[0] == "n":
            playAgain = False
            print("So no more Bingo today.  Thanks!")
        else:
            print("So let's play again...")


def main():
    """
    Main function
    """
    print("Game Player here...")
    # print(f"__name__ has a value of {__name__}.")
    play_bingo_games()

if __name__ == "__main__":
    main()