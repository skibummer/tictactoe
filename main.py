#imports
from endgame import end_game_check

# Start Conditions
row0 = ["⬜️", "⬜️", "⬜️"]
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
map = [row0, row1, row2]
print("     Column0  Column1  Column2")
print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")
game_continue = True
turns_taken = 0

# TODO 1. Account for a choice already being taken
# TODO 2. Add end game conditions
# TODO 3. UX improvements to prevent user from crashing game
# TODO 4. UI
# TODO
# TODO
# TODO

while game_continue:
    # Player 1's turn
    p1_column_choice = int(input("Player 1: Choose the column of your move. \n "))
    p1_row_choice = int(input("Player 1: Choose the row of your move.\n "))

    map[p1_row_choice][p1_column_choice] = "X    "
    turns_taken += 1
    print(f"turns_taken: {turns_taken}")
    #Show's update of player 1's move
    print("     Column0  Column1  Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")


    #Player 2's Move
    p2_column_choice= int(input("Player 2: Choose the column of your move. \n "))
    p2_row_choice = int(input("Player 2: Choose the row of your move.\n "))

    map[p2_row_choice][p2_column_choice] = "O    "
    #records player 2's move
    turns_taken += 1
    #Shows update of player 2's move
    print("     Column0  Column1  Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")