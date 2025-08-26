"""Utilities for the program input and validation will go here"""

def extract_size(size: str) -> tuple[int, int]:
    """Extract and validate the width and height from a size string. Raises a ValueError exception on fail."""
    width, height = map(int, size.split())
    return width, height

def extract_position(position: str) -> tuple[int, int, str]:
    """Extract and validate the x and y coordinates and direction from a position string. Raises a ValueError exception on fail."""
    x, y, direction = position.split()
    return int(x), int(y), direction

def validate_instructions(instructions: str):
    """Validate the format and length of the instructions. Raises a ValueError exception on fail."""
    pass
