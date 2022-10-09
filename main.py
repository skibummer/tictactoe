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
        # game_continue = False
        # Player 1 Turn
        if player_turn == "1":
            # Pl
            p1_row_choice = int(input("Player 1: Choose the row of your move. ('0', '1', or '2')\n "))
            p1_column_choice = int(input("Player 1: Choose the column of your move. ('0', '1', or '2')\n "))

            # checking if choice is valid.
            if p1_column_choice < 0 or p1_column_choice > 2 or p1_row_choice < 0 or p1_row_choice > 2:
                print(p1_row_choice,p1_column_choice)
                print("Try again")

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
            p2_row_choice = int(input("Player 2: Choose the row of your move.('0', '1', or '2')\n "))
            p2_column_choice = int(input("Player 2: Choose the column of your move. ('0', '1', or '2')\n "))

            if p2_column_choice < 0 or p2_column_choice > 2 or p2_row_choice < 0 or  p2_row_choice > 2:
                print("Try again")

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
