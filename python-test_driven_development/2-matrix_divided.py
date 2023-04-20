#!/usr/bin/python3
"""
This module contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Function divides all elements of a matrix

    :param matrix: matrix to divide (list of lists)
    :param div: divisor (int or float)

    :error
        - TypeError:  if matrix is not a list of integers or floats
        - TypeError: Each row must be of the same size
        - TypeError: div must be a number(integer or float)
        - ZeroDivisionError: div must be different from 0

    :return: new matrix (list of lists)
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(error_msg)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(error_msg)
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
    return [[round(element / div, 2) for element in row] for row in matrix]
