# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:51:05 2017

@author: meryem
"""

from random import randint

# Create board variable (empty)
board = []

# Create board as a 5x5 grid of O's
for x in range(0, 5):
    board.append(["O"] * 5)

# Print board with O's joined by spaces
def print_board(board):
    for row in board:
        print " ".join(row)

# Print welcome message and board
print "Let's play Battleship!"
print_board(board)

# Two functions to place a battleship at a random location on the board
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

# Place battleship at random location on board
ship_row = random_row(board)
ship_col = random_col(board)

# REMOVE FROM FINAL VERSION
# Print battleship location (for testing purposes only)
print "Battleship location: " + str(ship_row) + ", " + str(ship_col)

# Take user input for four turns
for turn in range(4):
    guess_row = int(raw_input("Guess Row:")) - 1 # Subtracting 1 from user input...
    guess_col = int(raw_input("Guess Column:")) - 1 # ...to convert to 0-4 system
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        # Need to jump out of loop here; else turns continue even after sinking!
        break
    else:
        if guess_row not in range(6) or \
        guess_col not in range(6):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"

print_board(board)
