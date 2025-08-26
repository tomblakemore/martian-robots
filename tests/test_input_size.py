from src.utils import extract_size
import pytest

def test_empty_size():
    with pytest.raises(ValueError):
        extract_size("")

def test_non_integer_size():
    with pytest.raises(ValueError):
        extract_size("foo bar")

def test_negative_size():
    with pytest.raises(ValueError):
        extract_size("-1 -1")

def test_max_size():
    with pytest.raises(ValueError):
        extract_size("51 51")

def test_valid_size():
    assert extract_size("5 3") == (5, 3)
