#!/usr/bin/python3
""" Module 9-student
"""


class Student():
    """ Defines a class"""
    def __init__(self, first_name, last_name, age):
        """ initialiase data """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object: """

        my_dict = {}
        if attrs is None:
            return self.__dict__

        if type(attrs) is list or all(type(i) is str for i in attrs):
            for i in attrs:
                try:
                    my_dict[i] = self.__dict__[i]
                except Exception:
                    pass
            return my_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:
        """
        for key in json:
            setattr(self, key, json[key])
