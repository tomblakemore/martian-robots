from src.utils import validate_instructions
import pytest

def test_instructions_format():
    with pytest.raises(ValueError):
        validate_instructions("LRFABC")

def test_max_length_instructions():
    with pytest.raises(ValueError):
        validate_instructions("F" * 101)

def test_valid_instructions():
    validate_instructions("RFRFRFRF")  # Raises no exceptions
