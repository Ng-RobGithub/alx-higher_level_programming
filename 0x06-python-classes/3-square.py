#!/usr/bin/python3
"""Module for the Square class."""

class Square:
    """Initialize a new square.

    Args:
    size (int): The size of the new square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Calculate the area of the square.

            Returns:
            int: The area of the square.
            """
            return (self.__size **2)
