from dataclasses import dataclass, field
from .robot import Robot

@dataclass
class Mars:
    x_max: int
    y_max: int
    robots: list[Robot] = field(default_factory=list)
    scents: set[tuple[int, int, str]] = field(default_factory=set)

    def add_robot(self, robot: Robot) -> None:
        """Add a robot to Mars. Raises an OutOfBoundsError if the robot is placed outside the boundaries."""
        if self.is_out_of_bounds(robot.x, robot.y):
            raise OutOfBoundsError("Robot has been placed outside the boundaries")
        self.robots.append(robot)

    def is_out_of_bounds(self, x: int, y: int) -> bool:
        """Determine if a point x, y is outside the boundaries."""
        return not (0 <= x <= self.x_max and 0 <= y <= self.y_max)

    def move_robots(self) -> None:
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
                current_position = (robot.x, robot.y, robot.direction)
                if current_position in self.scents:
                    continue  # If the robot is about to make a move to a a known scent, skip the move
                next_x, next_y = self.next_coordinates(current_position)
                if self.is_out_of_bounds(next_x, next_y):
                    self.scents.add(current_position)  # If the next move is out of bounds, add the current position to the scents
                    robot.mark_as_lost()
                    break
                robot.move_to_coordinates(next_x, next_y)

    def next_coordinates(self, current_position: tuple[int, int, str]) -> tuple[int, int]:
        """Get the next coordinates for a single forward move."""
        moves = {
            "N": lambda x, y: (x, y + 1),
            "E": lambda x, y: (x + 1, y),
            "S": lambda x, y: (x, y - 1),
            "W": lambda x, y: (x - 1, y)
        }
        current_x, current_y, direction = current_position
        return moves[direction](current_x, current_y)

    def robot_positions(self) -> list[str]:
        """Return the positions of all robots."""
        return [robot.position() for robot in self.robots]

# Exception for out of bounds errors
class OutOfBoundsError(Exception):
    pass
