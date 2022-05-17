#!/usr/bin/python3
"""Represents a Square.
    Private instance attribute: size
    Private instance attribute: position
    Instantiation with optional size and position
    Public instance method: area
    Public instance method: my_print """


class Square:
    """ Represents a class"""
    def __init__(self, size=0, position=0):
        """ Initialise the data."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieves the position."""
        return self.__postion

    @position.setter
    def position(self, value):
        """ Sets the position."""
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or not isinstance(value[1], int):
            raise TypeError("size must be an integer")

        self.__position = value

    def area(self):
        """ Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__size):
            print("")
        for row in range(0, self.__size):
            for hollow_col in range(self.__position[0]):
                print(" ", end="")
            for solid_col in range(0, self.__size):
                print('#', end="")
            print()
