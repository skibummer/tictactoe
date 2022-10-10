def new_game():
    def end_game_check():
        """"Checks win and tie conditions"""
        if row0[0] == row0[1] == row0[2] and row0[0] != "____":
            if row0[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row1[0] == row1[1] == row1[2] and row1[0] != "____":
            if row1[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row2[0] == row2[1] == row2[2] and row2[0] != "____":
            if row2[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row0[0] == row1[0] == row2[0] and row0[0] != "____":
            if row0[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row0[1] == row1[1] == row2[1] and row0[1] != "____":
            if row0[1] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row0[2] == row1[2] == row2[2] and row0[2] != "____":
            if row0[2] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row0[0] == row1[1] == row2[2] and row0[0] != "____":
            if row0[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row0[2] == row1[1] == row2[0] and row0[2] != "____":
            if row0[2] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif turns_taken == 9:
            print("Cats game!")
            return False

        else:
            return True

    # Set starting conditions and print screen
    row0 = ["____", "____", "____"]
    row1 = ["____", "____", "____"]
    row2 = ["____", "____", "____"]
    game_map = [row0, row1, row2]
    game_continue = True
    turns_taken = 0
    player_turn = "1"
    print("_____Column0_Column1_Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

    while game_continue:

        # check if Player 1 Turn
        if player_turn == "1":

            p1_coordinate_raw = input("Player 1: Choose the coordinate of your move. (for example, 11):  ")
            p1_coordinate_choice = str(p1_coordinate_raw)
            p1_row_choice = int(p1_coordinate_choice[0])
            p1_column_choice = int(p1_coordinate_choice[1])

            print(f"{p1_coordinate_choice}")

            # checking if choice is valid.
            if len(p1_coordinate_raw) != 2:
                print("Invalid input, will you please? try again")

            elif p1_column_choice < 0 or p1_column_choice > 2 or p1_row_choice < 0 or p1_row_choice > 2:
                print("Invalid input, will you please? try again")

            # checking if choice is already taken.
            elif game_map[p1_row_choice][p1_column_choice] != "____":
                print("That box is already chosen, pick an empty coordinate")

            # Show's update of player 1's move
            else:
                game_map[p1_row_choice][p1_column_choice] = "_X__"
                turns_taken += 1
                player_turn = "2"
                game_continue = end_game_check()
                print("     Column0  Column1  Column2")
                print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

        # Player 2's Move
        if player_turn == "2" and game_continue == True:

            p2_coordinate_raw = input("Player 2: Choose the coordinate of your move. (for example, 11):  ")
            p2_coordinate_choice = str(p2_coordinate_raw)
            p2_row_choice = int(p2_coordinate_choice[0])
            p2_column_choice = int(p2_coordinate_choice[1])
            print(f"{p2_coordinate_choice}")

            if len(p2_coordinate_raw) != 2:
                print("Invalid input, will you please? try again")

            elif p2_column_choice < 0 or p2_column_choice > 2 or p2_row_choice < 0 or p2_row_choice > 2:
                print(p2_row_choice, p2_column_choice)
                print("Invalid input, will you please? try again")

            elif game_map[p2_row_choice][p2_column_choice] != "____":
                print("That box is already chosen, pick an empty coordinate")

            else:
                game_map[p2_row_choice][p2_column_choice] = "_O__"
                # records player 2's move
                turns_taken += 1
                player_turn = "1"
                game_continue = end_game_check()
                # Shows update of player 2's move
                print("     Column0  Column1  Column2")
                print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

        # Ask for restart after game ends, resets to start conditions
        if not game_continue:
            if input("Would you like to play again? y/n\n") == "y":
                new_game()
            else:
                print("Goodbye")


new_game()
