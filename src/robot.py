from dataclasses import dataclass

@dataclass
class Robot:
    x: int
    y: int
    direction: str
    instructions: str = ""
    lost: bool = False

    def turn_left(self):
        """Turn the robot to the left."""
        directions = ["N", "W", "S", "E"]
        current_index = directions.index(self.direction)
        new_index = (current_index - 1) % 4
        self.direction = directions[new_index]

    def turn_right(self):
        """Turn the robot to the right."""
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % 4
        self.direction = directions[new_index]

    def move_to_coordinates(self, x: int, y: int):
        """Move the robot to a new position."""
        self.x = x
        self.y = y

    def mark_as_lost(self):
        """Mark the robot as lost."""
        pass

    def position(self) -> str:
        """Return the robot's current position as a string."""
        return f"{self.x} {self.y} {self.direction}" + (" LOST" if self.lost else "")
