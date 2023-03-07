#!/usr/bin/python3
# function that completes square if all integers of matrix


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list.map(lambda a: a ** 2, row))
    return new_matrix
