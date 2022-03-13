import os
import re
from pprint import pprint

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
    _history = tuple()

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
            command = input(
                "Enter your move ([a-h][0-7]) e.g. a1 a2: "
                "\n'exit' to end game"
                "\n'history' to view past moves"
                "\n-> "
            ).lower()

            # input validation
            print()
            if command == 'exit':
                print("exiting...")
                print()
                break
            elif command == 'history':
                print("\nhistory:\n")
                pprint(self._history)
                time.sleep(2)
                continue

            # prevent any invalid commands from breaking the code
            if not self.is_valid_move(command):
                continue



            # process valid input
            move = command.split(" ")
            current_pos = move[0][0], int(move[0][1])
            next_pos = move[1][0], int(move[1][1])
            piece = self.get_piece(current_pos)

            if type(piece) != str:
                # ensure there are no friendly pieces at destination location or pieces blocking the path
                if not self.is_blocked(current_pos, next_pos):
                    piece.curr_position = next_pos[0], next_pos[1]
                    # update board with the new position
                    self.chessboard[current_pos[1]][self._cood1[f"{current_pos[0]}"]] = " "
                    self.chessboard[next_pos[1]][self._cood1[f"{next_pos[0]}"]] = piece
                    # create new tuple with new command added
                    self.add_move(command)
                else:
                    continue
            else:
                print("Invalid position, there are no pieces at this location")
                print()
                time.sleep(2)
            self.refresh()

    def is_blocked(self, start_pos, end_pos):
        # first thing is to check that there are no friendly pieces at that location
        curr_piece = self.get_piece(start_pos)
        other_piece = self.get_piece(end_pos)
        if type(other_piece) != str and other_piece.colour == curr_piece.colour:
            print(f"Invalid move: there is a friendly chess piece at {end_pos}")
            time.sleep(2)
            return True

        # support jumping ability of knights, if the above condition is false, this must be true for knights only
        # since knights don't care about other pieces blocking their way
        if curr_piece.type == 'K':
            return False

        # prevent pawns from taking pieces in front of them
        # we've established that this must be the enemy
        if curr_piece.type == 'P' and curr_piece.colour == "White" and type(other_piece) != str:
            # if there is a piece directly in front of the pawn it cannot proceed
            if start_pos[1] + 1 == end_pos[1] and start_pos[0] == end_pos[0]:
                print("Invalid move: there is a chess piece blocking your path")
                time.sleep(2)
                return True
        elif curr_piece.type == 'P' and curr_piece.colour == "Black" and type(other_piece) != str:
            if start_pos[1] - 1 == end_pos[1] and start_pos[0] == end_pos[0]:
                print("Invalid move: there is a chess piece blocking your path")
                time.sleep(2)
                return True
        elif curr_piece.type == 'P' and type(other_piece) == str:
            if start_pos[0] != end_pos[0]:
                print("Invalid move: Pawns can move diagonally one space only when taking enemy pieces")
                time.sleep(2)
                return True
        elif curr_piece.type == 'P':
            return False

        # iterate towards target position, checking for pieces blocking the way that would invalidate move
        # convert to int indices using chr and ord e.g. chr(ord(curr_pos[0]) + 1) for ease of comparison
        curr_pos = list(start_pos)
        target_pos = list(end_pos)
        while curr_pos != target_pos:
            if self._cood1[f"{curr_pos[0]}"] < self._cood1[f"{target_pos[0]}"]:
                curr_pos[0] = chr(ord(curr_pos[0]) + 1)
            elif self._cood1[f"{curr_pos[0]}"] > self._cood1[f"{target_pos[0]}"]:
                curr_pos[0] = chr(ord(curr_pos[0]) - 1)

            if curr_pos[1] < target_pos[1]:
                curr_pos[1] += 1
            elif curr_pos[1] > target_pos[1]:
                curr_pos[1] -= 1

            # check for piece at curr_pos before it reaches its destination
            if type(self.get_piece(tuple(curr_pos))) != str and curr_pos != target_pos:
                print("Invalid move: there is a chess piece blocking your path")
                time.sleep(3)
                return True

        return False


    def is_valid_move(self, command):
        m = re.search(r'[a-h][0-7] [a-h][0-7]', command)
        if not m:
            print("Invalid input, please use format specified")
            time.sleep(1)
            return False
        return True

    def add_move(self, command):
        l = []
        for i in range(len(self._history)):
            l.append(self._history[i])
        l.insert(0, command)
        self._history = tuple(l)

    def get_piece(self, current_pos):
        # order of coordinates needs to be swapped due the rows representing numbers, not letters
        # [1-7][a-h]
        if current_pos[0] in self._cood1 and current_pos[1] in range(8):
            return self.chessboard[current_pos[1]][self._cood1[f"{current_pos[0]}"]]
        else:
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
            if i < len(self._history):
                print("{:7s}".format(self._history[i]), end="")
            else:
                print("{:7s}".format(""), end="")
            print(colors.WARNING, f"{i}", colors.ENDC, sep="", end=" ")
            i += 1
            for element in row:
                print("{:^4}|".format(element.__str__()), end=" ")

        print()
        print("{:9s}".format(""), end="")
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

if __name__ == '__main__':
    board = Board()
    board.set_up()
    board.run()


