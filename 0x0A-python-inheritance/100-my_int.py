#!/usr/bin/python3
"""
Module 100-my_int
"""


class MyInt(int):
    """MyInt is subclass of int
    with == and != operators inverted
    """

    def __eq__(self, other):
        """ Invert equality with inequality """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert inequality with equality """
        return super().__eq__(other)
