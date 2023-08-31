#!/usr/bin/python3

class Square:
    """Initialize a new square.

    Args:
    size (int): The size of the new square.
    """
    def __init__(self, size=0):
        self.__size = size

        @property
        def size(self):
            """Retrieve the size of the square."""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the square.

            Args:
            value (int): The new size value.
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Calculate the area of the square."""
                return self.__size ** 2

            def my_print(self):
                """Print the square with the character #."""
                if self.__size == 0:
                    print()

                else:
                for _ in range(self.__size):

                    print("#" * self.__size)
