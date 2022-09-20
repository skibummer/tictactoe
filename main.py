def end_game_check():
    if row0[0] == row0[1] == row0[2] and row0[0] != "⬜️":
        return False
    elif row1[0] == row1[1] == row2[2] and row1[0] != "⬜️":
        return False
    elif row2[0] == row2[1] == row2[2]  and row2[0] != "⬜️":
        return False
    elif row0[0] == row1[0] == row2[0]  and row0[0] != "⬜️":
        return False
    elif row0[1] == row1[1] == row2[1]  and row0[1] != "⬜️":
        return False
    elif row0[2] == row1[2] == row2[2]  and row0[2] != "⬜️":
        return False
    elif row0[0] == row1[1] == row2[2]  and row0[0] != "⬜️":
        return False
    elif row0[2] == row1[1] == row2[0]  and row0[2] != "⬜️":
        return False
    elif turns_taken == 9:
        return False
    else:
        return True

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
# TODO 5. add that rows and columns must be "X" or "O" ,not empty
# TODO
# TODO

while game_continue:
    game_continue = end_game_check()
    # Player 1's turn
    p1_column_choice = int(input("Player 1: Choose the column of your move. \n "))
    p1_row_choice = int(input("Player 1: Choose the row of your move.\n "))

    # checking if choice is already taken.

    # if choice is not taken/empty:
    #     then tell user its already taken
    #     have player to pick a different spot









    map[p1_row_choice][p1_column_choice] = "X    "
    turns_taken += 1
    game_continue = end_game_check()
    print(f"turns_taken: {turns_taken}")
    #Show's update of player 1's move
    print("     Column0  Column1  Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")


    #Player 2's Move
    if game_continue == True:
        p2_column_choice= int(input("Player 2: Choose the column of your move. \n "))
        p2_row_choice = int(input("Player 2: Choose the row of your move.\n "))

        map[p2_row_choice][p2_column_choice] = "O    "
        #records player 2's move
        turns_taken += 1
        game_continue = end_game_check()
        print(f"turns_taken: {turns_taken}")
        #Shows update of player 2's move
        print("     Column0  Column1  Column2")
        print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")
