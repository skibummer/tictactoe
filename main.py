class TicTacToe:
    def __init__(self):
        """Initialize game state"""
        self.row3 = ["_____", "_____", "_____"]
        self.row2 = ["_____", "_____", "_____"]
        self.row1 = ["_____", "_____", "_____"]
        self.game_map = [self.row1, self.row2, self.row3]
        self.game_continue = True
        self.turns_taken = 0
        self.player_turn = "1"

    def print_map(self):
        """Print current tic-tac-toe grid"""
        print("\nTic-tac-toe\n")
        print(f"3{self.row3}\n2{self.row2}\n1{self.row1}")
        print("_____1________2________3____\n")

    def end_game_check(self):
        """
        Define and check end of game conditions
        Print winner or tie then return false if game is over
        Return true if game is not over
        """
        # top row
        if self.row3[0] == self.row3[1] == self.row3[2] and self.row3[0] != "_____":
            if self.row3[0] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # middle row
        elif self.row2[0] == self.row2[1] == self.row2[2] and self.row2[0] != "_____":
            if self.row2[0] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # bottom row
        elif self.row1[0] == self.row1[1] == self.row1[2] and self.row1[0] != "_____":
            if self.row1[0] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # left column
        elif self.row3[0] == self.row2[0] == self.row1[0] and self.row3[0] != "_____":
            if self.row3[0] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # middle column
        elif self.row3[1] == self.row2[1] == self.row1[1] and self.row3[1] != "_____":
            if self.row3[1] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # right column
        elif self.row3[2] == self.row2[2] == self.row1[2] and self.row3[2] != "_____":
            if self.row3[2] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # diagonal bottom right to top left
        elif self.row3[0] == self.row2[1] == self.row1[2] and self.row3[0] != "_____":
            if self.row3[0] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # diagonal bottom left to top right
        elif self.row3[2] == self.row2[1] == self.row1[0] and self.row3[2] != "_____":
            if self.row3[2] == "__X__":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return False

        # tie if board is full and there are no winners
        elif self.turns_taken == 9:
            print("Cats game!")
            return False

        # no end of game conditions met
        else:
            return True

    def valid_input_check(self, coordinate, x_coord, y_coord):
        """Check if player input is somewhat valid"""

        # check if coordinate character length is 2
        if len(coordinate) != 2:
            print("Invalid input, will you please try again?")
            return False

        # check if coordinate given is within map range
        elif x_coord < 0 or x_coord > 2 or y_coord < 0 or y_coord > 2:
            print("Coordinate out of range, will you please try again?")

        # check if choice is already taken
        elif self.game_map[y_coord][x_coord] != "_____":
            print("That box is already chosen, pick an empty coordinate")
            return False

        # continue if input passes checks
        else:
            return True

    def mark_map(self, x_coord, y_coord):
        """Check which player turn
            Use appropriate mark
            Switch player turn
            Record turn taken
            Print map
            Check end game conditions
        """
        # Player 1
        if self.player_turn == "1":
            self.game_map[y_coord][x_coord] = "__X__"
            self.player_turn = "2"

        # Player 2
        elif self.player_turn == "2":
            self.game_map[y_coord][x_coord] = "__0__"
            self.player_turn = "1"

        self.turns_taken += 1
        self.print_map()
        self.game_continue = self.end_game_check()

    def game_core(self):

        self.print_map()
        while self.game_continue:

            # prompt player input
            coord_raw = input(f"Player {self.player_turn}: Choose a coordinate. (<X><Y>, for example, 11):  ")
            x_coord = int(coord_raw[0]) - 1
            y_coord = int(coord_raw[1]) - 1

            # check input validity
            if self.valid_input_check(coord_raw, x_coord, y_coord):

                # record player move and check end of game conditions
                self.mark_map(x_coord, y_coord)


# turn game on
game_on = True

while game_on:
    # name new instance of TicTacToe
    new_game = TicTacToe()
    # start new game
    new_game.game_core()

    if input("Would you like to play again? y/n: ") == "y":
        game_on = True
    else:
        print("Goodbye")
        game_on = False
