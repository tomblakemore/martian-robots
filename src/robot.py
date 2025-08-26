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
        pass # TODO: Implement this method

    def turn_right(self):
        """Turn the robot to the right."""
        pass # TODO: Implement this method

    def move_forward(self):
        """Move the robot forward by one in the direction it is facing."""
        pass # TODO: Implement this method

    def mark_as_lost(self):
        """Mark the robot as lost."""
        pass # TODO: Implement this method

    def position(self) -> str:
        """Return the robot's current position as a string."""
        return f"{self.x} {self.y} {self.direction}" + (" LOST" if self.lost else "")
