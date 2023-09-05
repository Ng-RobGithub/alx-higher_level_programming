#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute (default symbol)

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        self.__width = 0  # Private instance attribute for width
        self.__height = 0  # Private instance attribute for height

         #Use the setters to validate and set width and height

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1  # Increment the count on instance creation

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
                def area(self):
                    return self.__width * self.__height

                def perimeter(self):
                    return 2 * (self.__width + self.__height)

                def __str__(self):
                    if self.__width == 0 or self.__height == 0:
                        return ""
                    rectangle_str = ""
                    for _ in range(self.__height):
                        rectangle_str += str(self.print_symbol) * self.__width + "\n"
                        return rectangle_str[:-1]  # Remove the trailing newline character

                    def __repr__(self):
                        return f"Rectangle({self.__width}, {self.__height})"
                    
                    def __del__(self):
                        print("Bye rectangle...")
                        Rectangle.number_of_instances -= 1  # Decrement the count on instance deletion
