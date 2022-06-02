#!/usr/bin/python3
""" Module base"""
import json

class Base:
    """ Represent a class Base
    if id is not None increment __nb_objects and assign new value
    to the public instance attribute id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises data """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is not None or len(list_dictionary) == 0:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ +'.json'
        with open(filename, 'w') as f:
            json.dump(list_objs, f)
