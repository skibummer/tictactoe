# Tic-tac-toe

Welcome to my text based version of a tic-tac-toe game coded in python 3 and designed to run from a command line.


## Dependencies

Python 3.10.7

## Description

It prints a tic-tac-toe grid with labeled rows and columns. Two human players make choices by entering coordinates,
one integer at a time to refer to a row and column. The coordinates refer to a spot on the grid. If the coordinate is blank,
then whichever player has the current turn puts down their mark, either "_X__" or "_O__". If the coordinate is already taken,
the user will recieve a prompt to try again.

Player 1 always starts first with "`_X__`"
Player 2 always starts second with "`_O__`"

Players take turns until either someone wins or there is a tie.
A win is three marks in a straight line. That line can be horizontal, vertical, or diagonal on the game grid.

There is an option for a rematch at the end of a game.

## Getting Started

Enter the following into your preferred shell to get started.

`py main.py` or `python main.py`

If `python main.py` does not work, python wasn't added to PATH system or user  variable.
You can reinstall python and enable python being added to PATH.
