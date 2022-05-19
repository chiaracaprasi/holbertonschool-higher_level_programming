#!/usr/bin/python3
"""

Module add-integer
Adds two integer together

"""


def add_integer(a, b=98):
    """Returns the addition of a and b,
    a and b must be integers or floats otherwise error will occur
    a and b must be first casted to integers if they are float """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
