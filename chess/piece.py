# this class will represent any specified chess piece
# it will store the pieces current location and will be able
# to calculate the list of next possible locations based on board boundaries
# need to figure out a way to check if a piece is already at that location
from logging import exception


class Piece:
    types = {
        "P": "P",
        "R": "R",
        "K": "K",
        "B": "B",
        "Q": "Q",
        "K": "K"
    }
    cood1 = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    cood2 = [i for i in range(8)]

    def __init__(self, p_type, c1, c2):
        try:
            self.piece_type = self.types[f"{p_type}"]
            self.curr_position = (self.cood1[f"{c1}"], self.cood2[c2])
        except exception(BaseException) as e:
            print(f"Oops! invalid inputs! please check piece type {p_type} or positions {c1, c2} are valid")

    # needs  a method that determines what the acceptable movements are based on piece type

    # needs a method to set new position

