from game import Board


def start():
    print("Welcome to the Tic-Tac-Toe game!")

    # Create a board object
    board = Board()

    # Print the board
    board.get_board()

    # Start Game
    board.play()

    should_continue = input("Would you like to play another game? Type 'Y' or 'N': ")
    if should_continue.lower() == "n":
        print("Thanks for playing!")
    else:
        start()


start()
