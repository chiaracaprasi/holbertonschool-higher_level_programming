#!/usr/bin/python3
class Square:
    """Represents a Square.
    Private instance attribute: size
    Instantiation with size (no type/value verification)."""

    def __init__(self, size):
        """ Initialise the data."""
        self.__size = size
