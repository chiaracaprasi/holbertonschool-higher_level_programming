#!/usr/bin/python3
"""
Module 10-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a subclass of Rectangle"""
    def __init__(self, size):
        """instantiation of the rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area."""
        return self.__size ** 2
