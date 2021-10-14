"""Module to test dynamic classes"""
from dynamic import (
    Location, Direction, DirectionFlag, X_LIMIT, Y_LIMIT, get_direction_flag
)
import pytest


def test_location_default():
    p = Location()
    assert not p.is_valid()

def test_location_valid():
    p = Location(2,1)
    assert p.is_valid()

def test_location_limits_1():
    p = Location(20,1)
    assert not p.is_valid()

def test_location_limits_2():
    p = Location(20,1)
    assert not p.is_valid()
    p = p + Direction(DirectionFlag.east)
    assert p.x == X_LIMIT

def test_location_limits_3():
    p = Location(5,-10)
    assert not p.is_valid()
    p = p + Direction(DirectionFlag.north)
    assert p.x == X_LIMIT
    assert p.y == 0

def test_location_one_step():
    north = Direction(DirectionFlag.north)
    p = Location(0, 0)
    assert p.is_valid()
    p = p + north
    assert p.x == 0
    assert p.y == 1

def test_location_multi_step():
    east = Direction(DirectionFlag.east)
    p = Location(2, 0)
    assert p.is_valid()

    for i in range(1, 3):
        p = p + east

    assert p.x == X_LIMIT
    assert p.y == 0

def test_location_multi_direction_move():
    east = Direction(DirectionFlag.east)
    south = Direction(DirectionFlag.south)
    north = Direction(DirectionFlag.north)
    west = Direction(DirectionFlag.west)
    p = Location(0, 0)
    for i in range(1, 5):
        p = p + north
    for i in range(1, 5):
        p = p + east
    for i in range(1, 5):
        p = p + south
    for i in range(1, 5):
        p = p + west
    assert p.x == 0
    assert p.y == 0

def test_direction_right_rotation():
    north = Direction(DirectionFlag.north)
    assert north.x == 0
    assert north.y == 1
    north.rotate_right()
    assert north.flag == DirectionFlag.east

def test_direction_right_rotation_2():
    south = Direction(DirectionFlag.south)
    assert south.x == 0
    assert south.y == -1
    south.rotate_right()
    south.rotate_right()
    assert south.flag == DirectionFlag.north

def test_direction_left_rotation():
    west = Direction(DirectionFlag.west)
    assert west.x == -1
    assert west.y == 0
    west.rotate_left()
    assert west.flag == DirectionFlag.south

def test_direction_right_rotation_2():
    east = Direction(DirectionFlag.east)
    assert east.x == 1
    assert east.y == 0
    east.rotate_left()
    east.rotate_left()
    assert east.flag == DirectionFlag.west

def test_direction_flag_label():
    flag = get_direction_flag('NORTH')
    dir = Direction(flag)
    assert dir.flag == DirectionFlag.north