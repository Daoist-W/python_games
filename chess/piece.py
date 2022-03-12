# this class will represent any specified chess piece
# it will store the pieces current location and will be able
# to calculate the list of next possible locations based on board boundaries
# need to figure out a way to check if a piece is already at that location
import time
from logging import exception
from abc import abstractmethod, ABCMeta

from chess.colors import colors


class Piece(metaclass=ABCMeta):
    _types = {
        "P": "P",
        "R": "R",
        "K": "K",
        "B": "B",
        "Q": "Q",
        "E": "E"
    }
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
    _cood2 = [i for i in range(8)]

    def __init__(self, p_type, c1, c2, colour):
        self._colour = colour
        try:
            self._piece_type = self._types[f"{p_type}"]
            self._curr_position = (self._cood1[f"{c1}"], self._cood2[c2])
        except exception(BaseException) as e:
            print(f"Oops! invalid inputs! please check piece type {p_type} or positions {c1, c2} are valid")

    @abstractmethod
    def validate_move(self, c1, c2) -> bool:
        pass  # This will determine the possible positions for a given piece

    @property
    def curr_position(self):
        return self._curr_position

    @curr_position.setter
    def curr_position(self, curr_position: tuple):
        # This will only be called if move has been validated by Piece instance and
        # Validated by the chess board, which will check against other positions
        if self.validate_move(curr_position[0], curr_position[1]):
            self._curr_position = self._cood1[f"{curr_position[0]}"], curr_position[1]

    def __repr__(self):
        # TODO: Find a more robust solution for the string formatting
        if self._colour == "Black":
            s = str(f"{colors.OKBLUE} {self._piece_type}  {colors.ENDC}")
            return s
        else:
            s = str(f"{colors.HEADER} {self._piece_type}  {colors.ENDC}")
            return s


class Pawn(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="P", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: need to create different possible moves depending on player/color
            if self._colour == 'White':
                possible_moves = [
                    (self._curr_position[0], self._curr_position[1] + 1),
                    (self._curr_position[0] + 1, self._curr_position[1] + 1),
                    (self._curr_position[0] - 1, self._curr_position[1] + 1)
                ]
            else:
                possible_moves = [
                    (self._curr_position[0], self._curr_position[1] - 1),
                    (self._curr_position[0] + 1, self._curr_position[1] - 1),
                    (self._curr_position[0] - 1, self._curr_position[1] - 1)
                ]

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            int_to_str = (list(self._cood1.keys())[list(self._cood1.values()).index(self.curr_position[0])])

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                # fudge to get the value of a key from the number, I need to change that to enumaration
                # TODO: change cood1 to enum
                print(f"{self.__repr__()} "
                      f"{int_to_str, self.curr_position[1]} "
                      f"to {c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{self.__repr__()} "
                      f"{int_to_str, self.curr_position[1]} "
                      f"to {c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False


class Rook(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="R", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: test me!!
            horizontal_moves = [(i, self._curr_position[1]) for i in range(7)]
            vertical_moves = [(self._curr_position[0], j) for j in range(7)]
            possible_moves = horizontal_moves + vertical_moves

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                print(self._curr_position)
                print(f"{c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False


class Bishop(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="B", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            diagonal_moves1 = [(self._curr_position[0] + i, self._curr_position[1] + i) for i in range(7)]
            diagonal_moves2 = [(self._curr_position[0] - i, self._curr_position[1] - i) for i in range(7)]
            diagonal_moves3 = [(self._curr_position[0] - i, self._curr_position[1] + i) for i in range(7)]
            diagonal_moves4 = [(self._curr_position[0] + i, self._curr_position[1] - i) for i in range(7)]
            possible_moves = diagonal_moves1 + diagonal_moves2 + diagonal_moves3 + diagonal_moves4

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                print(self._curr_position)
                print(f"{c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False


class Knight(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="K", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!
            possible_moves = [
                (self._curr_position[0] + 1, self._curr_position[1] + 2),
                (self._curr_position[0] - 1, self._curr_position[1] + 2),
                (self._curr_position[0] + 1, self._curr_position[1] - 2),
                (self._curr_position[0] - 1, self._curr_position[1] - 2),
            ]

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                print(self._curr_position)
                print(f"{c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False


class King(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="E", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!
            possible_moves = [
                (self._curr_position[0] + 1, self._curr_position[1] + 1),
                (self._curr_position[0] - 1, self._curr_position[1] + 1),
                (self._curr_position[0] + 1, self._curr_position[1] - 1),
                (self._curr_position[0] - 1, self._curr_position[1] - 1),
                (self._curr_position[0], self._curr_position[1] + 1),
                (self._curr_position[0], self._curr_position[1] - 1),
                (self._curr_position[0] + 1, self._curr_position[1]),
                (self._curr_position[0] - 1, self._curr_position[1])
            ]

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                print(self._curr_position)
                print(f"{c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False


class Queen(Piece):

    def __init__(self, c1, c2, colour):
        super().__init__(p_type="Q", c1=c1, c2=c2, colour=colour)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!
            horizontal_moves = [(i, self._curr_position[1]) for i in range(7)]
            vertical_moves = [(self._curr_position[0], j) for j in range(7)]
            diagonal_moves1 = [(self._curr_position[0] + i, self._curr_position[1] + i) for i in range(7)]
            diagonal_moves2 = [(self._curr_position[0] - i, self._curr_position[1] - i) for i in range(7)]
            diagonal_moves3 = [(self._curr_position[0] - i, self._curr_position[1] + i) for i in range(7)]
            diagonal_moves4 = [(self._curr_position[0] + i, self._curr_position[1] - i) for i in range(7)]
            possible_moves = diagonal_moves1 + diagonal_moves2 + diagonal_moves3 + diagonal_moves4
            possible_moves += horizontal_moves + vertical_moves

            # filter out these moves to eliminate off-board positions
            valid_moves = [move for move in possible_moves if
                           move[0] in self._cood1.values() and
                           move[1] in self._cood2]

            if (self._cood1[f"{c1}"], self._cood2[c2]) in valid_moves:
                print(self._curr_position)
                print(f"{c1, c2} is a valid move!")
                return True
            else:
                print(self._curr_position)
                print(f"{c1, c2} is NOT a valid {self.__repr__()} move!")
                time.sleep(2)
                return False
