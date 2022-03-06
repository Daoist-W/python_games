# this file contains tests for the piece.py file
import pytest
from chess.piece import Pawn


def test_position():
    p = Pawn("a", 1, "Black")
    assert p.curr_position == (0, 1)


def test_position_invalid_row():
    with pytest.raises(Exception) as e_info:
        p = Pawn("a", 10, "Black")


def test_position_invalid_column():
    with pytest.raises(Exception) as e_info:
        p = Pawn("p", 1, "Black")


def test_valid_move():
    p = Pawn("a", 1, "Black")
    assert p.validate_move("a", 2) is True


def test_invalid_move():
    p = Pawn("a", 1, "Black")
    assert p.validate_move("a", 3) is False


