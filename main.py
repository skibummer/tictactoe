def game_core():
    """TicTacToe"""
    def end_game_check():
        """"Define and check end of game conditions"""
        if row3[0] == row3[1] == row3[2] and row3[0] != "____":
            if row3[0] == "_X__":
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

        elif row1[0] == row1[1] == row1[2] and row1[0] != "____":
            if row1[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row3[0] == row2[0] == row1[0] and row3[0] != "____":
            if row3[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row3[1] == row2[1] == row1[1] and row3[1] != "____":
            if row3[1] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row3[2] == row2[2] == row1[2] and row3[2] != "____":
            if row3[2] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row3[0] == row2[1] == row1[2] and row3[0] != "____":
            if row3[0] == "_X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        elif row3[2] == row2[1] == row1[0] and row3[2] != "____":
            if row3[2] == "_X__":
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

        elif x_cord < 0 or x_cord > 2 or y_cord < 0 or y_cord > 2:
            print("Coordinate out of range, will you please try again?")

        # check if choice is already taken
        elif game_map[y_cord][x_cord] != "____":
            print("That box is already chosen, pick an empty coordinate")
            return False
        # continue turn if input is somewhat valid
        else:
            return True

    def mark_map(x_coord, y_coord):
        """Check which player turn and use appropriate mark"""
        # test
        # print(f"player_turn {player_turn}")
        # print(f"turns_taken {turns_taken}")

        if player_turn == "1":
            game_map[y_coord][x_coord] = "_X__"

        elif player_turn == "2":
            game_map[y_coord][x_coord] = "_0__"

        # print(f"turns_taken: {turns_taken}")
        # update game map with player move

    # Set start conditions
    row3 = ["____", "____", "____"]
    row2 = ["____", "____", "____"]
    row1 = ["____", "____", "____"]
    game_map = [row1, row2, row3]
    game_continue = True
    turns_taken = 0
    player_turn = "1"

    print(f"Row3{row3}\nRow2{row2}\nRow1{row1}")
    print("_____Column1_Column2_Column3")

    # game loop/core
    while game_continue:

        # check if Player 1 turn
        if player_turn == "1":

            p1_coord_raw = input("Player 1: Choose the coordinate of your move. (<X><Y>, for example, 11):  ")
            p1_x_coord = int(p1_coord_raw[0])-1
            p1_y_coord = int(p1_coord_raw[1])-1

            # test input
            # print(p1_coord_raw)
            # print(f"test p1_x_coord: {p1_x_coord}")
            # print(f"test p1_y_coord: {p1_y_coord}")

            if valid_input_check(p1_coord_raw, p1_x_coord, p1_y_coord):
                """If input is somewhat valid, finish player 1 turn"""
                mark_map(p1_x_coord, p1_y_coord)
                turns_taken += 1
                # print(f"turns_taken:{turns_taken}")
                player_turn = "2"
                game_continue = end_game_check()
                print(f"Row3{row3}\nRow2{row2}\nRow1{row1}")
                print("_____Colum1_Column2_Column3")

        # check if Player 2's turn
        if player_turn == "2" and game_continue == True:

            p2_coord_raw = input("Player 2: Choose the coordinate of your move. (<X><Y>, for example, 11):  ")
            p2_x_coord = int(p2_coord_raw[0])-1
            p2_y_coord = int(p2_coord_raw[1])-1

            # test input
            # print(p2_coord_raw)

            if valid_input_check(p2_coord_raw, p2_x_coord, p2_y_coord):
                # record player 2's move and check end of game conditions
                mark_map(p2_x_coord, p2_y_coord)
                turns_taken += 1
                print(turns_taken)
                player_turn = "1"
                game_continue = end_game_check()
                print(f"Row3{row3}\nRow2{row2}\nRow1{row1}")
                print("_____Column1_Column2_Column3")

        # ask for restart after game ends, resets to start conditions if yes
        if not game_continue:
            if input("Would you like to play again? y/n: ") == "y":
                game_core()
            else:
                print("Goodbye")
game_core()
