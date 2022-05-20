#!/usr/bin/python3
"""

Module matrix-divide
Divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """Returns a new matrix(list of list of int or float)
    with result of division of matrix by div rounded to 2 dec places
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDisionError("division by zero")

    new_list = []

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                 raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(n / div, 2))

    print (new_list)
