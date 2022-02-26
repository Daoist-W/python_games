from pprint import pprint
from chess.piece import Pawn, Rook, Knight, Bishop, King, Queen


# this class will represent the chess board
# it will contain a 2D array with chess pieces

class Board:

    def __init__(self):
        self.chessboard = [[" " for i in range(8)] for j in range(8)]

    # method to set up the board
    def set_up(self):
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
            Rook('a', 0, "Black"),
            Knight('b', 0, "Black"),
            Bishop('c', 0, "Black"),
            King('d', 0, "Black"),
            Queen('e', 0, "Black"),
            Bishop('f', 0, "Black"),
            Knight('g', 0, "Black"),
            Rook('h', 0, "Black")
        ]

    # method to set the board, this will move the Pieces based on their current location
    # to their destination location, if this location is valid

    # method to print the current state of the board
    def display(self):
        for row in self.chessboard:
            print()
            print()
            for element in row:
                print("{:^4}|".format(element.__str__()), end=" ")




    # there should be a tuple that stores move history, so we can trace back movements made


board = Board()
board.set_up()
board.display()
