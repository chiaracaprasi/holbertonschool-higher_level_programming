#!/usr/bin/python3
"""Represents a class rectangle."""


class Rectangle:
    """"Represents a class rectangle define by width and height .
    Private instance attribute: width
    Instantiation with optional wiidth and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialise the data."""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieves the data."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the data."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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

    def area(self):
        """ Returns the rectangle area."""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        """ Setting to print the rectangle with the character """
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            return '\n'.join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print 'Bye rectangle...'
        when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
