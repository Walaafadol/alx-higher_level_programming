#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
    @property
    def size(self):
        """property new Square.

        raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
        """
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Initialize area of Square.


        Returns:
        area of square.
        """
        return self.__size **2
