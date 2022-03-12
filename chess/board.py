import os

from chess.colors import colors
from chess.piece import Pawn, Rook, Knight, Bishop, King, Queen

import time


# this class will represent the chess board
# it will contain a 2D array with chess pieces

class Board:
    _cood1 = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    def __init__(self):
        self.chessboard = [[" " for i in range(8)] for j in range(8)]

    # method to run the game
    def run(self):
        # handle user input, passing on the commands to relevant objects/methods
        # will continuously listen with a while loop until user enters exit or cancels
        os.system('cls')
        print()
        print("Terminal Based Chess Game (Python) v1.0")
        print()
        time.sleep(1)
        self.display()
        print()
        while True:
            # TODO: Exception handling for incorrect input
            command = input(
                "Enter your move ([a-h][0-7]) e.g. a1 a2: "
                "\n'exit' to end game"
                "\n'history' to view past moves"
                "\n-> "
            )
            print()
            if command == 'exit':
                print("exiting...")
                print()
                break

            # TODO: Prevent anything that isn't valid input from passing here
            move = command.split(" ")
            current_pos = move[0][0], int(move[0][1])
            next_pos = move[1][0], int(move[1][1])
            piece = self.get_piece(current_pos)
            if type(piece) != str:
                piece.curr_position = next_pos[0], next_pos[1]
            else:
                print("Invalid position, there are no pieces at this location")
                print()
                time.sleep(2)
            self.refresh()

    def get_piece(self, current_pos):
        # order of coordinates needs to be swapped due the rows representing numbers, not letters
        # [1-7][a-h]
        print(current_pos[0], current_pos[1])
        if current_pos[0] in self._cood1 and current_pos[1] in range(8):
            return self.chessboard[current_pos[1]][self._cood1[f"{current_pos[0]}"]]
        else:
            print("invalid position")
            return " "

    # method to set up the board
    def set_up(self):
        # the indices have to be swapped in order, [1][0] when calling object from chessboard
        self.chessboard[1] = [Pawn(c1, c2, "White") for c1, c2 in
                              [(i, 1) for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]]
        self.chessboard[6] = [Pawn(c1, c2, "Black") for c1, c2 in
                              [(i, 6) for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]]

        self.chessboard[0] = [
            Rook('a', 0, "White"),
            Knight('b', 0, "White"),
            Bishop('c', 0, "White"),
            King('d', 0, "White"),
            Queen('e', 0, "White"),
            Bishop('f', 0, "White"),
            Knight('g', 0, "White"),
            Rook('h', 0, "White")
        ]

        self.chessboard[7] = [
            Rook('a', 7, "Black"),
            Knight('b', 7, "Black"),
            Bishop('c', 7, "Black"),
            King('d', 7, "Black"),
            Queen('e', 7, "Black"),
            Bishop('f', 7, "Black"),
            Knight('g', 7, "Black"),
            Rook('h', 7, "Black")
        ]

    # method to set the board, this will move the Pieces based on their current location
    # to their destination location, if this location is valid

    # method to print the current state of the board
    def display(self):
        os.system('cls')
        print()
        print("Terminal Based Chess Game (Python) v1.0")
        print()
        i = 0
        for row in self.chessboard:
            print()
            print(colors.WARNING, f"{i}", colors.ENDC, sep="", end=" ")
            i += 1
            for element in row:
                print("{:^4}|".format(element.__str__()), end=" ")

        print()
        print(" ", end=" ")
        for element in self._cood1.keys():
            print(colors.WARNING, "{:^4} ".format(element), colors.ENDC, sep="", end=" ")
        print()
        print()

    def refresh(self):
        # create a copy array and loop through the old one, continually shifting the
        # pieces to their new positions
        # this is going to require validation
        new_chessboard = [[" " for i in range(8)] for j in range(8)]
        for row in self.chessboard:
            for element in row:
                if type(element) != str:
                    position = element.curr_position
                    new_chessboard[position[1]][position[0]] = element

        self.chessboard = new_chessboard
        self.display()


# there should be a tuple that stores move history, so we can trace back movements made

board = Board()
board.set_up()

board.run()
