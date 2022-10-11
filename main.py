def game_core():
    """TicTacToe"""
    def end_game_check():
        """"Defines and checks end of game conditions"""
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

    def valid_input_check(coordinate, x_cord, y_cord):
        """Check if player input is somewhat valid"""
        # check if coordinate given is within map range
        if len(coordinate) != 2:
            print("Invalid input, will you please try again?")
            return False

        # check if choice is already taken
        elif game_map[x_cord][y_cord] != "____":
            print("That box is already chosen, pick an empty coordinate")
            return False
        # pass value if somewhat valid
        else:
            return True

    # Set start conditions
    row0 = ["____", "____", "____"]
    row1 = ["____", "____", "____"]
    row2 = ["____", "____", "____"]
    game_map = [row0, row1, row2]
    game_continue = True
    turns_taken = 0
    player_turn = "1"
    print("_____Column0_Column1_Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

    # game loop/core
    while game_continue:

        # check if Player 1 turn
        while player_turn == "1":

            p1_coord_raw = input("Player 1: Choose the coordinate of your move. (row,column, for example, 11):  ")
            p1_x_cord = int(p1_coord_raw[0])
            p1_y_cord = int(p1_coord_raw[1])

            # test
            print(f"{p1_coord_raw}")

            # check if input is valid character length
            if valid_input_check(p1_coord_raw, p1_x_cord, p1_y_cord):
                """If input is somewhat valid, finish player 1 turn"""
                game_map[p1_x_cord][p1_y_cord] = "_X__"
                turns_taken += 1
                player_turn = "2"
                game_continue = end_game_check()
                print("     Column0  Column1  Column2")
                print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

        # check if Player 2's turn
        while player_turn == "2" and game_continue == True:

            p2_coordinate_raw = input("Player 2: Choose the coordinate of your move. (row,column, for example, 11):  ")
            p2_coordinate_choice = str(p2_coordinate_raw)
            p2_row_choice = int(p2_coordinate_choice[0])
            p2_column_choice = int(p2_coordinate_choice[1])
            print(f"{p2_coordinate_choice}")

            # check if input is valid character length
            if len(p2_coordinate_raw) != 2:
                print("Invalid input, will you please? try again")

            # check if coordinate given is within map range
            elif p2_column_choice < 0 or p2_column_choice > 2 or p2_row_choice < 0 or p2_row_choice > 2:
                print(p2_row_choice, p2_column_choice)
                print("Invalid input, will you please? try again")

            # check if choice is already taken
            elif game_map[p2_row_choice][p2_column_choice] != "____":
                print("That box is already chosen, pick an empty coordinate")

            # update and print player 1's move
            else:
                game_map[p2_row_choice][p2_column_choice] = "_O__"
                # records player 2's move
                turns_taken += 1
                player_turn = "1"
                game_continue = end_game_check()
                # Shows update of player 2's move
                print("     Column0  Column1  Column2")
                print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

        # ask for restart after game ends, resets to start conditions if yes
        if not game_continue:
            if input("Would you like to play again? y/n: ") == "y":
                game_core()
            else:
                print("Goodbye")
game_core()
