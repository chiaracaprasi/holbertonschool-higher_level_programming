#!/usr/bin/python3
"""

Module print_square
Prints a square with the character #

"""


def print_square(size):
    """Prints a sqaure with #
    Size miust be an integer and => 0 otherwise error will occur
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print('#', end="")
        print()
