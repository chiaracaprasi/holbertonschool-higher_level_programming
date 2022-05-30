#!/usr/bin/python3
""" Contains function 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Checks if object is object is an instance of,
    or if object is an instance of class inherited from, the specified class
    and returns True, otherwise False
    """
    if not isinstance(obj, a_class):
        return False
    return True
