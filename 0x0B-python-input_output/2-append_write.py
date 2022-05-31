#!/usr/bin/python3
""" Module 2-append_write.py """


def append_write(filename="", text=""):
    """ Writes a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, "a") as f:
        return f.write(text)
