from src.robot import Robot

def test_turning_right():
    robot = Robot(0, 0, "N")
    robot.turn_right()
    assert robot.direction == "E"
    robot.turn_right()
    assert robot.direction == "S"
    robot.turn_right()
    assert robot.direction == "W"
    robot.turn_right()
    assert robot.direction == "N"

def test_turning_left():
    robot = Robot(0, 0, "N")
    robot.turn_left()
    assert robot.direction == "W"
    robot.turn_left()
    assert robot.direction == "S"
    robot.turn_left()
    assert robot.direction == "E"
    robot.turn_left()
    assert robot.direction == "N"
