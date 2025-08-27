from src.mars import Mars, OutOfBoundsError
from src.robot import Robot
import pytest

def test_adding_robots():
    mars = Mars(5, 3)
    robot = Robot(0, 0, "N")
    mars.add_robot(robot)
    assert robot in mars.robots

def test_out_of_bounds():
    mars = Mars(5, 3)
    with pytest.raises(OutOfBoundsError):
        mars.add_robot(Robot(10, 10, "N"))
