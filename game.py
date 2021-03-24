class Board:
    def __init__(self):
        self.board = {"1": " ", "2": " ", "3": " ",
                      "4": " ", "5": " ", "6": " ",
                      "7": " ", "8": " ", "9": " ",
                      }

        self.current_turn = "O"

    def get_board(self):
        print(f"{self.board['1']} | {self.board['2']} | {self.board['3']}")
        print("---------")
        print(f"{self.board['4']} | {self.board['5']} | {self.board['6']}")
        print("---------")
        print(f"{self.board['7']} | {self.board['8']} | {self.board['9']}")

    def play(self):
        # Check the board for winning combinations
        # Return the function if one of the players has won or entire board is filled.
        if self.check_board(self.current_turn):
            return

        self.change_current_turn()
        position = input(f"{self.current_turn} turn. Enter position from 1-9: ")
        self.place_marker(position, self.current_turn)

    def change_current_turn(self):
        if self.current_turn == "X":
            self.current_turn = "O"
        else:
            self.current_turn = "X"

    def place_marker(self, position, marker):
        if int(position) > 9:
            print("That number is too high! Try again.")
            # Change current turn, so it can then be changed back in the Play function (current play continues).
            self.change_current_turn()

        elif self.board[position] == " ":
            # Places a marker if the given position is empty
            self.board[position] = marker
            self.get_board()
        else:
            print("Position taken! Please enter another number.")
            self.change_current_turn()

        self.play()

    def check_board(self, marker):
        # There are 8 possible winning combinations in a 3x3 game of Tic-tac-toe.

        # CHECK HORIZONTALS
        if (self.board["1"] == marker and self.board["2"] == marker and self.board["3"] == marker or
                self.board["4"] == marker and self.board["5"] == marker and self.board["6"] == marker or
                self.board["7"] == marker and self.board["8"] == marker and self.board["9"] == marker):

            print(f"Game Over! {marker} Wins!")
            return True

        # CHECK VERTICALS
        if (self.board["1"] == marker and self.board["4"] == marker and self.board["7"] == marker or
                self.board["2"] == marker and self.board["5"] == marker and self.board["8"] == marker or
                self.board["3"] == marker and self.board["6"] == marker and self.board["9"] == marker):

            print(f"Game Over! {marker} Wins!")
            return True

        # CHECK DIAGONALS
        if (self.board["1"] == marker and self.board["5"] == marker and self.board["9"] == marker or
                self.board["3"] == marker and self.board["5"] == marker and self.board["7"] == marker):

            print(f"Game Over! {marker} Wins!")
            return True

        # CHECK DRAW
        elif all(value != " " for value in self.board.values()):
            print("Game over! It's a tie!")
            return True
