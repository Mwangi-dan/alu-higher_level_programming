#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row != len(matrix):
            for j in range(len(row)):
                if j == len(row):
                    print("{:d}".format(row[j]))
                else:
                    print("{:d}".format(row[j]), end=" ")
        print()
