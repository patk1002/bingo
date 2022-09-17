#! /usr/env python
"""
This is to play bingo
Some ideas came from https://stackoverflow.com/questions/69601220/bingo-using-python
"""

import numpy as np
import random

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

# def print_card(card):

#     for letter in card:
#         print(letter, end="\t")
#         for number in card[letter]:
#             print(number, end="\t")
#         print("\n")
#     print("\n")

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
    title = ["B", "I", "N", "G", "O"]
    card = np.array(([1, 16, 31, 46, 61],
                     [2, 17, 32, 47, 62],
                     [3, 18, 33, 48, 63],
                     [4, 19, 34, 49, 64],
                     [5, 20, 35, 50, 65]))
    return card


def print_card(card):
    """
    Print the Bingo card
    """
    print("Now printing the card as it is.")
    print(card)


def playBingoGame():
    """
    Play one Bingo game here
    """
    print("\nLet's play Bingo now...")
    card = generate_card()
    print("\nHere is your card:\n")
    print_card(card)
    print("Now you can enter the Bingo number, play, check for Bingo, and loop.")


def playBingoGames():
    """
    Play multiple Bingo games, asking after each to continue or not
    """
    playAgain = True
    while (playAgain):
        playBingoGame()
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
    playBingoGames()

if __name__ == "__main__":
    main()