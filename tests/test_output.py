from src.mars import Mars, OutOfBoundsError
from src.robot import Robot
import pytest

def test_out_of_bounds():
    mars = Mars(5, 3)
    with pytest.raises(OutOfBoundsError):
        mars.add_robot(Robot(10, 10, "N"))

def test_simple_moves():
    mars = Mars(5, 3)
    mars.add_robot(Robot(0, 0, "N", "FRF"))
    mars.move_robots()
    assert mars.robot_positions() == ["1 1 E"]

def test_sample_cases_no_scents():
    mars = Mars(5, 3)
    robots = [
        Robot(1, 1, "E", "RFRFRFRF"),
        Robot(3, 2, "N","FRRFLLFFRRFLL")
    ]
    for robot in robots:
        mars.add_robot(robot)
    mars.move_robots()
    assert mars.robot_positions() == [
        "1 1 E",
        "3 3 N LOST"
    ]
