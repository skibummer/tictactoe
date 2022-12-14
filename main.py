def end_game_check():
    """"Checks win and tie conditions"""
    if row0[0] == row0[1] == row0[2] and row0[0] != "⬜️":
        if row0[0] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row1[0] == row1[1] == row2[2] and row1[0] != "⬜️":
        if row1[0] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row2[0] == row2[1] == row2[2]  and row2[0] != "⬜️":
        if row2[0] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row0[0] == row1[0] == row2[0]  and row0[0] != "⬜️":
        if row0[0] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row0[1] == row1[1] == row2[1]  and row0[1] != "⬜️":
        if row0[1] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row0[2] == row1[2] == row2[2]  and row0[2] != "⬜️":
        if row0[2] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row0[0] == row1[1] == row2[2]  and row0[0] != "⬜️":
        if row0[0] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif row0[2] == row1[1] == row2[0]  and row0[2] != "⬜️":
        if row0[2] == "X    ":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return False

    elif turns_taken == 9:
        print("Cats game!")
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
player_turn = "1"

# TODO UX/UI improvements to prevent user from crashing game


while game_continue:
    #Player 1 Turn
    if player_turn == "1" and game_continue == True:
        p1_row_choice = int(input("Player 1: Choose the row of your move. ('0', '1', or '2')\n "))
        p1_column_choice = int(input("Player 1: Choose the column of your move. ('0', '1', or '2')\n "))

        # checking if choice is valid.
        if p1_column_choice < 0 or p1_column_choice > 2 or p1_row_choice < 0 or  p1_row_choice > 2:
            print("Will you please try again")

        # checking if choice is already taken.
        elif map[p1_row_choice][p1_column_choice] != "⬜️":
            print("That box is already chosen, pick an empty coordinate")

        # Show's update of player 1's move
        else:
            map[p1_row_choice][p1_column_choice] = "X    "
            turns_taken += 1
            player_turn = "2"
            game_continue = end_game_check()
            print("     Column0  Column1  Column2")
            print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")


    #Player 2's Move
    if player_turn == "2" and game_continue == True:
        p2_row_choice = int(input("Player 2: Choose the row of your move.('0', '1', or '2')\n "))
        p2_column_choice = int(input("Player 2: Choose the column of your move. ('0', '1', or '2')\n "))

        if p2_column_choice < 0 or p2_column_choice > 2 or p2_row_choice < 0 or  p2_row_choice > 2:
            print("Try again")

        elif map[p2_row_choice][p2_column_choice] != "⬜️":
            print("That box is already chosen, pick an empty coordinate")

        else:
            map[p2_row_choice][p2_column_choice] = "O    "
            #records player 2's move
            turns_taken += 1
            player_turn = "1"
            game_continue = end_game_check()
            #Shows update of player 2's move
            print("     Column0  Column1  Column2")
            print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

    #Ask for restart after game ends, resets to start conditions
    if not game_continue:
        if input("Would you like to play again? y/n") == "y":
            game_continue = True
            turns_taken = 0
            player_turn = "1"
            row0 = ["⬜️", "⬜️", "⬜️"]
            row1 = ["⬜️", "⬜️", "⬜️"]
            row2 = ["⬜️", "⬜️", "⬜️"]
            print("     Column0  Column1  Column2")
            print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")
