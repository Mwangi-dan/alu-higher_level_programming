#!/usr/bin/python3
"""
Pascal's triangle principle
"""


def pascal_triangle(n):
    """
    Represents Pascal's Triangle of size n

    Returns a list of lists of integeres representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tru[i] + tri[i + 1])
            tmp.append(1)
            triangles.append(tmp)
        return triangles
