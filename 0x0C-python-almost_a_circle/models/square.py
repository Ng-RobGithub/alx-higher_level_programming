#!/usr/bin/python3
"""
This is the "square" module.
The square module supplies one class, Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a square."""


def __init__(self, size, x=0, y=0, id=None):
    """Initialize a new Square.

    Args:
    size (int): The size of the square.
    x (int, optional): The x-coordinate of the square's position.
    y (int, optional): The y-coordinate of the square's position.
    id (int, optional): The identifier for the square.

    """
    super().__init__(size, size, x, y, id)


@property
def size(self):
    """Get the size of the square."""
    return self.width


@size.setter
def size(self, value):
    """Set the size of the square.

    Args:
    value (int): The size of the square.

    Raises:
    ValueError: If `value` is not a positive integer.
    TypeError: If `value` is not an integer.

    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.width = value
    self.height = value


def __str__(self):
    """Return a string representation of the Square instance."""
    return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)


def area(self):
    """Return the area value of the Square instance."""
    return self.width * self.width


def update(self, *args, **kwargs):
    """Update the attributes of the Square instance.

    Args:
    *args: A variable-length list of arguments in the following order:
    1st argument should be the id attribute.
    2nd argument should be the size attribute.
    3rd argument should be the x attribute.
    4th argument should be the y attribute.
    **kwargs: A dictionary containing key-value pairs where each key
    represents an attribute to update and its associated value.

    """
    if args:
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
    else:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


def to_dictionary(self):
    """Return the dictionary representation of the Square instance."""
    return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
