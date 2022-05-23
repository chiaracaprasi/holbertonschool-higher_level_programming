#!/usr/bin/python3
"""
Represents a class rectangle.
"""


class Rectangle:
    """"Represents a class rectangle define by width and height """

    def __init__(self, width=0, height=0):
        """ Initialise the data."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Retrieves the size."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        """ Retrieves the data."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the data."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height
