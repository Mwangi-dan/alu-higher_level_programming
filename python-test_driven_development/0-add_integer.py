#!/usr/bin/python3

"""
This module contains the add_integer function
"""

def add_integer(a, b=98):
    """
    Adds two integers

    :param a: first integer
    :param b: second integer (default 98)

    :error: TypeError if a or b are not integers or floats

    :return: the sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
    
    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")