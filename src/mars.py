from dataclasses import dataclass, field
from .robot import Robot

@dataclass
class Mars:
    x_max: int
    y_max: int
    robots: list[Robot] = field(default_factory=list)
    scents: set[tuple[int, int, str]] = field(default_factory=set)

    def add_robot(self, robot: Robot):
        """Add a robot to Mars. Raises an OutOfBoundsError if the robot is placed outside the boundaries."""
        if not self.is_within_the_boundaries(robot.x, robot.y):
            raise OutOfBoundsError("Robot has been placed outside the boundaries")
        self.robots.append(robot)

    def is_within_the_boundaries(self, x: int, y: int) -> bool:
        """Determine if a point x, y is within the boundaries."""
        return True  # TODO: Implement this method

    def move_robots(self):
        """Move all robots, in the order they were added, according to their instructions."""
        pass  # TODO: Implement this method

    def robot_positions(self) -> list[str]:
        """Return the positions of all robots."""
        return [robot.position() for robot in self.robots]

class OutOfBoundsError(Exception):
    pass
