import enum

X_LIMIT = 4
Y_LIMIT = 4


class DirectionFlag(enum.Enum):
    north = 1
    east = 2
    south = 3
    west = 4

def get_direction_flag(label):
    """convert string to a direction flag."""
    if label == 'NORTH':
        return DirectionFlag.north
    elif label == 'EAST':
        return DirectionFlag.east
    elif label == 'SOUTH':
        return DirectionFlag.south
    elif label == 'WEST':
        return DirectionFlag.west
    else:
        raise ValueError(f'Invalid label for direction: {label}')

class Direction:
    """Class to handle direction vector."""

    def __init__(self, flag):
        """Initialize direction values."""
        self.flag = flag
        self.__refresh()

    def rotate_right(self):
        """Rotates direction flag clockwise and updates vector values."""
        if self.flag == DirectionFlag.north:
            self.flag = DirectionFlag.east
        elif self.flag == DirectionFlag.east:
            self.flag = DirectionFlag.south
        elif self.flag == DirectionFlag.south:
            self.flag = DirectionFlag.west
        elif self.flag == DirectionFlag.west:
            self.flag = DirectionFlag.north
        self.__refresh()

    def rotate_left(self):
        """Rotates direction flag anti-clockwise and updates vector values."""
        if self.flag == DirectionFlag.north:
            self.flag = DirectionFlag.west
        elif self.flag == DirectionFlag.east:
            self.flag = DirectionFlag.north
        elif self.flag == DirectionFlag.south:
            self.flag = DirectionFlag.east
        elif self.flag == DirectionFlag.west:
            self.flag = DirectionFlag.south
        self.__refresh()

    def get_label(self):
        """convert direction to a string value."""
        if self.flag == DirectionFlag.north:
            return 'NORTH'
        elif self.flag == DirectionFlag.east:
            return 'EAST'
        elif self.flag == DirectionFlag.south:
            return 'SOUTH'
        elif self.flag == DirectionFlag.west:
            return 'WEST'

    def __refresh(self):
        """Updates direction values x,y according to its flag."""
        if self.flag == DirectionFlag.north:
            self.x = 0
            self.y = 1
        elif self.flag == DirectionFlag.east:
            self.x = 1
            self.y = 0
        elif self.flag == DirectionFlag.south:
            self.x = 0
            self.y = -1
        elif self.flag == DirectionFlag.west:
            self.x = -1
            self.y = 0
        else:
            raise ValueError("Invalid direction flag")

class Location:
    """Class to handle location point x,y."""

    def __init__(self, x = -1, y = -1):
        """Initialize location with values or -1 if not defined."""
        self.x = x
        self.y = y

    def __add__(self, o):
        """Add two Locations."""
        self.x = self.x + o.x
        self.y = self.y + o.y
        self.__refresh()
        return self

    def is_valid(self):
        """Check if location is within acceptable limits."""
        return self.x >= 0 and self.x <= X_LIMIT and self.y >= 0 and self.y <= Y_LIMIT

    def __refresh(self):
        """Reset location if its outside limits"""
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > X_LIMIT:
            self.x = X_LIMIT
        if self.y > Y_LIMIT:
            self.y = Y_LIMIT

