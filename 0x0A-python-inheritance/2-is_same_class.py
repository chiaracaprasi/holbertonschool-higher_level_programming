#!/usr/bin/python3
""" Contains function 2-is_same_class """


def is_same_class(obj, a_class):
    """ Checks if object is exactly an instance of the specified class
    and returns True, otherwise False
    """
    return type(obj) == a_class
