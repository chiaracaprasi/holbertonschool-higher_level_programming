#!/usr/bin/python3
""" Module base"""
import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file """
        my_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for item in list_objs:
                my_list.append(cls.to_dictionary(item))
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set """
        dummy = cls(1, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + '.json'
        my_list = []
        try:
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
                for key, value in enumerate(my_list):
                    my_list[key] = cls.create(**my_list[key])
        except Exception:
            pass
        return my_list
