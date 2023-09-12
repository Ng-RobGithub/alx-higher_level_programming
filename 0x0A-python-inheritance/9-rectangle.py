#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle."""

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            return self.__width * self.__height
        """Return the area of the rectangle."""

        def __str__(self):
            """Return the print() and str() representation of a Rectangle."""
            return (f"[Rectangle] {self.__width}/{self.__height}")
