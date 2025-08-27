# 🤖 Martian Robots

A [Python](https://www.python.org) implementation of Martian Robots. Martian Robots simulates robots exploring the Martian landscape. Users define the size of Mars, place robots on it, and supply each robot with a sequence of instructions. The program will then calculate the final positions of the robots, running each of the instructions in order.

## Approach

1. **Initial Setup**: Create an empty project with a virtual environment and initial structure.
2. **Simple Cases**: Start by writing simple test cases for the Mars and Robot classes to ensure they behave as expected.
3. **Losses & Scents Cases**: Next, write tests followed by the logic for handling robot losses and marking scents on the Mars grid.
4. **Input Handling**: Write tests and methods for extracting and validating the input.
5. **Output Formatting**: Finally, complete the main program entry point to prompt the user for the input and display the output.

## Project Structure

The program source files can be found in the `src` directory and the test files in the `tests` directory.

Within the `src` directory:

- Mars and Robot classes are defined in `mars.py` and `robot.py`, respectively
- Utility functions for extracting and validating input are defined in `utils.py`
- The main entry point for the program is `main.py`

Within the `Mars` class:

- The boundary is defined by the `x_max` and `y_max` attributes
- The placed robots are stored in the `robots` attribute
- The scents (positions where robots have fallen off the grid) are stored in the `scents` attribute
- Methods are provided for adding robots and moving robots, which handles the losses and scents
- An additional method is provided for retrieving the positions of all robots

Within the `Robot` class:

- The current position is defined by the `x` and `y` attributes
- The current direction is defined by the `direction` attribute
- The instructions for movement are defined by the `instructions` attribute
- Methods are provided for turning the robot, moving to a new position, and marking the robot as lost
- An additional method is provided for formatting the final position

Within the `main.py` file:

- On execution, the user is first prompted to enter the size of the Mars grid
- The user is then prompted to enter the initial positions, directions, and movement instructions for the robots
- One or many robots can be added, until the "finish" command is given
- The final positions are then calculated and displayed

## Getting Started

Check out the repository and move to the root directory.

Install Python 3.13 then, inside the root directory, create the virtual environment:

```bash
python3.13 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

## Running

To run the program:

```bash
python -m src.main
```

To run the tests:

```bash
pytest tests
```
