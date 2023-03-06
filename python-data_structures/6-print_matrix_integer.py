#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]))
            print(end="\n" if j == len(matrix[i]) - 1 else " ")
        print()
