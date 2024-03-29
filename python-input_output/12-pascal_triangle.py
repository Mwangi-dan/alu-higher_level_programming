#!/usr/bin/python3
"""
Pascal's triangle principle
"""


def pascal_triangle(n):
    """
    Represents Pascal's Triangle of size n

    Returns a list of lists of integeres representing the triangle
    """
    li = []
    if n <= 0:
        return li
    for r in range(n):
        for c in range(r + 1):
            if c == 0:
                li.append([1])
            elif c == r:
                li[r].append(1)
            else:
                li[r].append(li[r - 1][c] + li[r - 1][c - 1])
        return li
