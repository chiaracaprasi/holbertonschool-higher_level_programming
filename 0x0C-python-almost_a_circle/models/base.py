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
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to CSV file """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Square":
                    for o in list_objs:
                        writer.writerow([o.id, o.size, o.x, o.y])
                if cls.__name__ == "Rectangle":
                    for o in list_objs:
                        writer.writerow([o.id, o.width, o.height, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialisation in CSV, returns a list of instances"""
        filename = cls.__name__ + '.csv'
        my_list = []
        try:
            with open(filename, 'r') as cvsfile:
                reader = csv.reader(csvfile)
                for i in reader:
                    if cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]),
                                      "size": int(args[1]),
                                      "x": int(args[2]),
                                      "y": int(args[3])}
                    elif cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}

                    obj = cls.create(**dictionary)
                    my_list.append(obj)
                    return my_list
        except Exception:
            return my_list
