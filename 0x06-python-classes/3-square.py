#!/usr/bin/python3
"""Represents a Square.
    Private instance attribute: size
    Public instance method: area
    Instantiation with optional size"""


class Square:
    """ Represents a class"""
    def __init__(self, size=0):
        """ Initialise the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the current square area."""
        return self.__size ** 2
