#!/usr/bin/python3
"""
Module 12-pascal_triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of int representing Pascal’s triangle of n """

    my_list = []

    for i in range(n):
        my_list.append([1] * (i + 1))

    for i in range(2, n):
        for j in range(1, i):
            my_list[i][j] = my_list[i - 1][j - 1] + my_list[i - 1][j]

    return my_list
