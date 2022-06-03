#!/usr/bin/python3
"""
Module append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """" Append new_string after search_string in filename """
    with open(filename, 'r', encoding='utf-8') as read_file:
        text = read_file.readlines()

    with open(filename, 'w', encoding='utf-8') as write_file:
        my_string = ""
        for line in text:
            if search_string in line:
                my_string = my_string + new_string
            my_string = my_string + line
        write_file.write(my_string)
