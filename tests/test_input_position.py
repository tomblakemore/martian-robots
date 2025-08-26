from src.utils import extract_position
import pytest

def test_empty_position():
    with pytest.raises(ValueError):
        extract_position("")

def test_non_integer_coordinates():
    with pytest.raises(ValueError):
        extract_position("foo bar N")

def test_negative_coordinates():
    with pytest.raises(ValueError):
        extract_position("-1 -1 N")

def test_max_coordinates():
    with pytest.raises(ValueError):
        extract_position("51 51 N")

def test_direction():
    with pytest.raises(ValueError):
        extract_position("1 1 Z")

def test_valid_position():
    assert extract_position("1 1 E") == (1, 1, "E")
