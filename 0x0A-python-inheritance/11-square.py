#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new square."""
        super().__init__(size, size)

        def __str__(self):
            """Return the square description."""
            return "[Square] {}/{}".format(self.__size, self.__size)
