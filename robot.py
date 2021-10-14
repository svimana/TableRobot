"""Module to handle TableRobot class"""
from dynamic import (
    Location, Direction, DirectionFlag, X_LIMIT, Y_LIMIT
)

class TableRobot:
    """Class to handle Table Robot activity."""

    def __init__(self):
        self.location = Location()
        self.direction = Direction(DirectionFlag.north)

    def is_on_table(self):
        """Flag to indicate if the robot has valid location."""
        return self.location.is_valid()

    def place(self, new_location: Location, new_direction: Direction):
        """Place the robot on the new location and direction if the location is valid.
            If location is valid, current location and direction get updated
        """
        if not new_location.is_valid():
           return False

        self.location = new_location
        self.direction = new_direction

        return True

    def move(self):
        """Moves the robot one step according to the current direction.
            If it's going to go over the table area, its location will not be changed.
        """
        self.location = self.location + self.direction

    def left(self):
        """Rotate the robot to the left."""
        self.direction.rotate_left()

    def right(self):
        """Rotate the robot to the right."""
        self.direction.rotate_right()

    def print_position(self):
        """Print the current location and direction to a string."""
        return f'{self.location.x},{self.location.y},{self.direction.get_label()}'