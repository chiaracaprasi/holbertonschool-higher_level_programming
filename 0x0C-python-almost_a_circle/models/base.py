#!/usr/bin/python3
""" Module base"""


class Base:
    """ Represent a class Base
    if id is not None increment __nb_objects and assign new value
    to the public instance attribute id"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
