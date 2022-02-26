# this class will represent any specified chess piece
# it will store the pieces current location and will be able
# to calculate the list of next possible locations based on board boundaries
# need to figure out a way to check if a piece is already at that location
from logging import exception
from abc import abstractmethod, ABCMeta


class Piece(metaclass=ABCMeta):
    _types = {
        "P": "P",
        "R": "R",
        "KN": "KN",
        "B": "B",
        "Q": "Q",
        "K": "K"
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

    def __init__(self, p_type, c1, c2, player):
        self._player = player
        try:
            self._piece_type = self._types[f"{p_type}"]
            self._curr_position = (self._cood1[f"{c1}"], self._cood2[c2])
        except exception(BaseException) as e:
            print(f"Oops! invalid inputs! please check piece type {p_type} or positions {c1, c2} are valid")

    @abstractmethod
    def validate_move(self, c1, c2) -> bool:
        pass  # This will determine the possible positions for a given piece

    def set_curr_position(self, c1, c2):
        # This will only be called if move has been validated by Piece instance and
        # Validated by the chess board, which will check against other positions
        if self.validate_move(c1, c2):
            self._curr_position = (c1, c2)

    def __repr__(self):
        return self._piece_type


class Pawn(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="P", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            possible_moves = [
                (self._curr_position[0], self._curr_position[1] + 1),
                (self._curr_position[0] + 1, self._curr_position[1] + 1),
                (self._curr_position[0] - 1, self._curr_position[1] + 1)
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
                print(f"{c1, c2} is NOT a valid move!")
                return False


class Rook(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="R", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!

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
                print(f"{c1, c2} is NOT a valid move!")
                return False


class Bishop(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="B", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!

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
                print(f"{c1, c2} is NOT a valid move!")
                return False


class Knight(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="KN", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!

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
                print(f"{c1, c2} is NOT a valid move!")
                return False


class King(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="K", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!

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
                print(f"{c1, c2} is NOT a valid move!")
                return False


class Queen(Piece):

    def __init__(self, c1, c2, player):
        super().__init__(p_type="Q", c1=c1, c2=c2, player=player)

    def validate_move(self, c1, c2) -> bool:

        # calculate list of legal positions, filter them out based on board boundaries
        # if c1 and c1 are valid, return true, else return false
        if c1 in self._cood1 and c2 in self._cood2:
            # list of possible moves that can be taken by this piece
            # TODO: implement me!!

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
                print(f"{c1, c2} is NOT a valid move!")
                return False




