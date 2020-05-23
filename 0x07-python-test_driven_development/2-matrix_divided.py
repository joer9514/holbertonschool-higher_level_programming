#!/usr/bin/python3
"""
Return a new matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_marix = []
    tmp_lists = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        tmp_lists = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(msg)
            else:
                tmp_lists.append(round(items / div, 2))
        new_marix.append(tmp_lists)
    return new_marix
