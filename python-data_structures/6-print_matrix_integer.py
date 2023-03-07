#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d} ".format(matrix[row][col]), end="")
        if row != len(matrix):
            print()
