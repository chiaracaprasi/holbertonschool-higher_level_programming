#!/usr/bin/python3
""" Module 0-read_file """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout """
    with open("my_file_0.txt") as f:
        text = f.read()

    print(text)
