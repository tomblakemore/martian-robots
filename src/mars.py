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
        return 0 <= x <= self.x_max and 0 <= y <= self.y_max

    def move_robots(self):
        """Move all robots, in the order they were added, according to their instructions."""
        for robot in self.robots:
            for instruction in robot.instructions:
                change_direction = {
                    "L": robot.turn_left,
                    "R": robot.turn_right
                }
                if instruction in change_direction:
                    change_direction[instruction]()
                    continue
                next_x, next_y = self.next_coordinates(robot.x, robot.y, robot.direction)
                robot.move_to_coordinates(next_x, next_y)

    def next_north_coordinates(self, current_x: int, current_y: int) -> tuple[int, int]:
        """Get the next coordinates for a single forward move to the north."""
        return current_x, current_y + 1

    def next_coordinates(self, current_x: int, current_y: int, direction: str) -> tuple[int, int]:
        """Get the next coordinates for a single forward move."""
        moves = {
            "N": self.next_north_coordinates,
            "E": self.next_east_coordinates,
            "S": self.next_south_coordinates,
            "W": self.next_west_coordinates
        }
        return moves[direction](current_x, current_y)

    def next_north_coordinates(self, current_x: int, current_y: int) -> tuple[int, int]:
        """Get the next coordinates for a single forward move to the north."""
        return current_x, current_y + 1

    def next_east_coordinates(self, current_x: int, current_y: int) -> tuple[int, int]:
        """Get the next coordinates for a single forward move to the east."""
        return current_x + 1, current_y

    def next_south_coordinates(self, current_x: int, current_y: int) -> tuple[int, int]:
        """Get the next coordinates for a single forward move to the south."""
        return current_x, current_y - 1

    def next_west_coordinates(self, current_x: int, current_y: int) -> tuple[int, int]:
        """Get the next coordinates for a single forward move to the west."""
        return current_x - 1, current_y

    def robot_positions(self) -> list[str]:
        """Return the positions of all robots."""
        return [robot.position() for robot in self.robots]

class OutOfBoundsError(Exception):
    pass
