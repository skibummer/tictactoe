def game_core():
    """TicTacToe"""
    def end_game_check():
        """"Define and check end of game conditions"""
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

    def valid_input_check(coordinate, y_cord, x_cord):
        """Check if player input is somewhat valid"""
        # check if coordinate given is within map range
        if len(coordinate) != 2:
            print("Invalid input, will you please try again?")
            return False

        elif x_cord < 0 or x_cord > 2 or y_cord < 0 or y_cord > 2:
            print(y_cord, x_cord)
            print("Invalid input, will you please? try again")

        # check if choice is already taken
        elif game_map[y_cord][x_cord] != "____":
            print("That box is already chosen, pick an empty coordinate")
            return False
        # continue turn if input is somewhat valid
        else:
            return True

    def mark_map(y_coord, x_coord, turns):
        """Check which player turn and use appropriate mark"""
        # test
        # print(f"player_turn {player_turn}")
        # print(f"turns_taken {turns_taken}")

        if player_turn == "1":
            game_map[y_coord][x_coord] = "_X__"

        elif player_turn == "2":
            game_map[y_coord][x_coord] = "_0__"

        # print(f"turns_taken {turns_taken}")
        # update game map with player move
        print("     Column0  Column1  Column2")
        print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

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

            p1_coord_raw = input("Player 1: Choose the coordinate of your move. (<row><column>, for example, 11):  ")
            p1_y_coord = int(p1_coord_raw[0])
            p1_x_coord = int(p1_coord_raw[1])
            # test input
            print(p1_coord_raw)

            if valid_input_check(p1_coord_raw, p1_y_coord, p1_x_coord):
                """If input is somewhat valid, finish player 1 turn"""
                mark_map(p1_y_coord, p1_x_coord)
                turns_taken += 1
                print(turns_taken)
                player_turn = "2"
                game_continue = end_game_check()

        # check if Player 2's turn
        while player_turn == "2" and game_continue == True:

            p2_coord_raw = input("Player 2: Choose the coordinate of your move. (<row><column>, for example, 11):  ")
            p2_y_coord = int(p2_coord_raw[0])
            p2_x_coord = int(p2_coord_raw[1])
            # test input
            print(p2_coord_raw)

            if valid_input_check(p2_coord_raw, p2_y_coord, p2_x_coord):
                # record player 2's move and check end of game conditions
                mark_map(p2_y_coord, p2_x_coord)
                turns_taken += 1
                print(turns_taken)
                player_turn = "1"
                game_continue = end_game_check()

        # ask for restart after game ends, resets to start conditions if yes
        if not game_continue:
            if input("Would you like to play again? y/n: ") == "y":
                game_core()
            else:
                print("Goodbye")
game_core()
