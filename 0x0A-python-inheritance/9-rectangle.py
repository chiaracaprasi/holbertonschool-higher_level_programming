#!/usr/bin/python3
"""
Module 9-rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
