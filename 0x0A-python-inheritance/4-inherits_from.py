#!/usr/bin/python3
""" Contains function 4-inherits_from"""


def inherits_from(obj, a_class):
    """ Checks if object is an instance of
    class that inherited (directly or indirectly) from the specified class
    and returns True, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
