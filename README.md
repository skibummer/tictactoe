# Tic-tac-toe

Welcome to my text based version of a tic-tac-toe game coded in python 3 and designed to run from a shell.


## Dependencies

Python 3.8

## Description

It prints a tic-tac-toe grid (3x3) with rows and columns, labeled 1 to 3, left to right, down to up. 
Coordinates of the grid are referred to by two digit coordinates such as 11,
which would refer to the bottom left part of the grid.

If the coordinate is blank,
then whichever player has the current turn puts down their mark, either "`__X__`" or "`__O__`".
If the coordinate is already taken, the user will receive a prompt to try again.

Player 1 always starts first with "`__X__`". Player 2 always starts second with "`__O__`"

Players take turns until either someone wins or there is a tie.
A win is three marks in a straight line.
That line can be horizontal, vertical, or diagonal on the game grid.

There is an option for a rematch at the end of a game.

## Getting Started

Enter the following into your preferred shell to get started.

`py main.py` or `python main.py`

If `python main.py` does not work, python wasn't added to PATH system or user  variable.
You can reinstall python and enable python being added to PATH.
