"""Module to test robot classes"""
from dynamic import (
    Location, Direction, DirectionFlag, X_LIMIT, Y_LIMIT
)
from robot import TableRobot
import pytest


def test_robot_default_position():
    robot = TableRobot()
    assert not robot.is_on_table()

def test_robot_valid_placement():
    robot = TableRobot()
    robot.place(Location(2,2), Direction(DirectionFlag.south))
    assert robot.is_on_table()

def test_robot_invalid_placement():
    robot = TableRobot()
    robot.place(Location(-1, -1), Direction(DirectionFlag.north))
    assert not robot.is_on_table()

def test_robot_invalid_placement_2():
    robot = TableRobot()
    robot.place(Location(20, 20), Direction(DirectionFlag.north))
    assert not robot.is_on_table()

def test_robot_movement_1():
    robot = TableRobot()
    robot.place(Location(0, 0), Direction(DirectionFlag.east))
    robot.move()
    robot.move()
    robot.move()
    assert robot.location.x == 3
    assert robot.location.y == 0
    assert robot.direction.flag == DirectionFlag.east

def test_robot_movement_limit():
    robot = TableRobot()
    robot.place(Location(1, 1), Direction(DirectionFlag.west))
    robot.move()
    robot.move()
    robot.move()
    assert robot.location.x == 0
    assert robot.location.y == 1
    assert robot.direction.flag == DirectionFlag.west

def test_robot_movement_and_rotation():
    robot = TableRobot()
    robot.place(Location(2, 0), Direction(DirectionFlag.north))
    robot.move()
    robot.move()
    robot.left()
    robot.left()
    robot.move()
    robot.move()
    # should come to the same position
    assert robot.location.x == 2
    assert robot.location.y == 0
    assert robot.direction.flag == DirectionFlag.south

def test_robot_position_label():
    robot = TableRobot()
    robot.place(Location(1, 2), Direction(DirectionFlag.south))
    robot.move()
    robot.left()
    robot.move()
    robot.move()
    assert robot.print_position() == '3,1,EAST'

def test_robot_position_label_2():
    robot = TableRobot()
    robot.place(Location(1, 1), Direction(DirectionFlag.north))
    robot.move()
    robot.right()
    robot.move()
    robot.move()
    robot.left()
    robot.move()
    assert robot.print_position() == '3,3,NORTH'