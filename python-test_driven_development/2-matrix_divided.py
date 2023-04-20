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
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
