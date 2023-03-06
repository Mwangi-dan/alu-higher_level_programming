#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            if col < len(row) - 1:
                print("{:d}".format(row[col]), end=' ')
            else:
                print("{:d}".format(row[col]), end='\n')
        print()
