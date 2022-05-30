#!/usr/bin/python3
"""
Module 11-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a subclass of Rectangle"""
    def __init__(self, size):
        """instantiation of the rectangle"""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area."""
        return self.size ** 2

    def __str__(self):
        """Informal string representation of the square"""
        return (f"[Square] {self.size}/{self.size}")
