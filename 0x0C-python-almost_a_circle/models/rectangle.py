#!/usr/bin/python3
"""
This is the "rectangle" module.
The rectangle module supplies one class, Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle."""


def __init__(self, width, height, x=0, y=0, id=None):
    """Initialize a new Rectangle.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int, optional): The x-coordinate of the rectangle's position.
    y (int, optional): The y-coordinate of the rectangle's position.
    id (int, optional): The identifier for the rectangle.

    """
    super().__init__(id)
    self.width = width
    self.height = height
    self.x = x
    self.y = y


@property
def width(self):
    """Get the width of the rectangle."""
    return self.__width


@width.setter
def width(self, value):
    """Set the width of the rectangle.

    Args:
        value (int): The width of the rectangle.

        Raises:
            ValueError: If `value` is not a positive integer.
            TypeError: If `value` is not an integer.

            """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value


@property
def height(self):
    """Get the height of the rectangle."""
    return self.__height


@height.setter
def height(self, value):
    """Set the height of the rectangle.

    Args:
        value (int): The height of the rectangle.

        Raises:
            ValueError: If `value` is not a positive integer.
            TypeError: If `value` is not an integer.

            """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value <= 0:
        raise ValueError("height must be > 0")
    self.__height = value


@property
def x(self):
    """Get the x-coordinate of the rectangle's position."""
    return self.__x


@x.setter
def x(self, value):
    """Set the x-coordinate of the rectangle's position.

    Args:
        value (int): The x-coordinate of the rectangle's position.

        Raises:
            ValueError: If `value` is not a negative integer.
            TypeError: If `value` is not an integer.

            """
    if not isinstance(value, int):
        raise TypeError("x must be an integer")
    if value < 0:
        raise ValueError("x must be >= 0")
    self.__x = value


@property
def y(self):
    """Get the y-coordinate of the rectangle's position."""
    return self.__y


@y.setter
def y(self, value):
    """Set the y-coordinate of the rectangle's position.

    Args:
    value (int): The y-coordinate of the rectangle's position.

    Raises:
    ValueError: If `value` is not a negative integer.
    TypeError: If `value` is not an integer.

    """
    if not isinstance(value, int):
        raise TypeError("y must be an integer")
    if value < 0:
        raise ValueError("y must be >= 0")
    self.__y = value


def area(self):
    """Return the area value of the Rectangle instance."""
    return self.__width * self.__height


def display(self):
    """Print the Rectangle instance with the character #."""
    for i in range(self.__y):
        print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)


def __str__(self):
    """Return a string representation of the Rectangle instance."""
    return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)


def update(self, *args, **kwargs):
    """Update the attributes of the Rectangle instance.

    Args:
    *args: A variable-length list of arguments in the following order:
    1st argument should be the id attribute.
    2nd argument should be the width attribute.
    3rd argument should be the height attribute.
    4th argument should be the x attribute.
    5th argument should be the y attribute.
    **kwargs: A dictionary containing key-value pairs where each key
    represents an attribute to update and its associated value.

    """
    if args:
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
    else:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


def to_dictionary(self):
    """Return the dictionary representation of the Rectangle instance."""
    return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
