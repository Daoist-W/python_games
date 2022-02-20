# this file contains tests for the piece.py file
import pytest
from chess import piece


def test_position():
    p = piece.Piece("P", "a", 1)
    assert p.curr_position == (0, 1)


def test_position_invalid_row():
    with pytest.raises(Exception) as e_info:
        p = piece.Piece("P", "a", 10)


def test_position_invalid_column():
    with pytest.raises(Exception) as e_info:
        p = piece.Piece("P", "p", 1)


def test_more():
    # TODO: implement me!
    pass
