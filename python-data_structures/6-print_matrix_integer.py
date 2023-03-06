#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row != len(matrix):
            print()
        for col in range(len(row)):
            print("{:d} ".format(row[col]), end="")
