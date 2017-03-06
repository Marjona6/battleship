# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:51:05 2017

@author: meryem
"""
# VERSION: Multiple battleships
# Default variables below:
ships = 1

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

# Here is the while condition so we can make sure to get a good number of ships
ships_good = False # condition defaults to false
while ships_good == False:
    # Request user input: how many battleships?
    print "How many battleships would you like?"
    ships = int(raw_input("Enter a number from 1 to 3: "))
    # Test that it is an appropriate number of ships
    if ships in range(1,4): # Range set for humans, not machines
        print "Thank you. Let's get started!"
        ships_good = True # makes the condition true
    else:
        print "Not a valid entry. Please try again."

# Use user-input number of ships desired to randomly place ships on board
ship_row = []
ship_col = []
for n in range(ships+1):
    # Place one battleship at random location on board
    ship_row[n] = random_row[n](board)
    ship_col[n] = random_col[n](board)

    # REMOVE FROM FINAL VERSION
    # Print battleship location (for testing purposes only)
    print "Battleship location: " + str(ship_row[n]) + ", " + str(ship_col[n])
'''
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
'''