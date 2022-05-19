#!/usr/bin/python3
"""

Module say_my_name
Prints My name is first_name followed byt last name

"""


def say_my_name(first_name, last_name=""):
    """ prints My name is followed by first name and last name
    first_name and last_name must be strings otherwise error will occur
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
