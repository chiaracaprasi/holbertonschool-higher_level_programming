#!/usr/bin/python3
"""Module 101-add_attribute
"""


def add_attribute(obj, attr, value):
    """ adds a new attribute to an object if it’s possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
