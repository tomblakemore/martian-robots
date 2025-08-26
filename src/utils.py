"""Utilities for the program input and validation will go here"""

def extract_size(size: str) -> tuple[int, int]:
    """Extract and validate the width and height from a size string. Raises a ValueError exception on fail."""
    width, height = map(int, size.split())
    if not (0 <= width < 50 and 0 <= height < 50):
        raise ValueError("The maximum size is 50")
    return width, height

def extract_position(position: str) -> tuple[int, int, str]:
    """Extract and validate the x and y coordinates and direction from a position string. Raises a ValueError exception on fail."""
    x, y, direction = position.split()
    if not (0 <= int(x) < 50 and 0 <= int(y) < 50):
        raise ValueError("The maximum position is 50, 50")
    if direction not in ["N", "E", "S", "W"]:
        raise ValueError("Invalid direction")
    return int(x), int(y), direction

def validate_instructions(instructions: str):
    """Validate the format and length of the instructions. Raises a ValueError exception on fail."""
    if not all(char in ["L", "R", "F"] for char in instructions):
        raise ValueError("Invalid instructions characters")
    if len(instructions) > 100:
        raise ValueError("Instructions are too long")
