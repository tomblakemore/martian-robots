from .mars import Mars
from .robot import Robot
from .utils import extract_size, extract_position, validate_instructions

def build_mars() -> Mars:
    """Create Mars by asking for the size."""
    width, height = prompt_for_size()
    return Mars(width, height)

def prompt_for_size() -> tuple[int, int]:
    """Prompt for the grid size of Mars."""
    prompt = "Enter the grid size of Mars, or \"exit\" to quit: "
    while True:
        size = input(prompt)
        if size.lower() == "exit":
            exit()
        try:
            return extract_size(size)
        except ValueError:
            prompt = "Invalid size format. Please try again in \"width height\" format: "

def add_robots_to_mars(mars: Mars) -> list[Robot]:
    """Add one or many robots to Mars by asking for their positions and instructions."""

    # Prompt for the first robot's position
    prompt = "Enter the position of the first robot: "
    while True:
        position = input(prompt)
        if position.lower() == "exit":
            exit()
        if position.lower() == "finish":
            break
        try:
            x, y, direction = extract_position(position)
        except ValueError:
            prompt = "Invalid position. Please try again in \"x y direction\" format: "
            continue

        # Check if the position is within the boundaries of Mars
        if mars.is_out_of_bounds(x, y):
            prompt = "Position is out of bounds. Please try again: "
            continue

        # Prompt for this robot's instructions and add the robot to Mars
        mars.add_robot(Robot(x, y, direction, prompt_for_instructions()))

        # Prompt for next robot, or "finish" to start moving them
        prompt = "Enter the position of the next robot, or \"finish\" to calculate the final positions: "

def prompt_for_instructions() -> str:
    """Prompt for the instructions for a robot."""
    prompt = "Enter the instructions for this robot: "
    while True:
        instructions = input(prompt)
        if instructions.lower() == "exit":
            exit()
        try:
            validate_instructions(instructions)
            return instructions
        except ValueError:
            prompt = "Invalid instructions. Please try again: "

def main():
    """Main entry point for the program."""
    mars = build_mars()
    add_robots_to_mars(mars)
    mars.move_robots()
    print("Final positions:")
    for position in mars.robot_positions():
        print(position)

if __name__ == "__main__":
    main()
