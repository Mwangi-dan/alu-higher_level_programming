#!/usr/bin/python3
"""
is same class function
"""


def is_same_class(obj, a_class):
    """
    Checks if object is exactly an instance of specified class

    Argvs:
        obj: (class object)
        a_class: (name of class)

    Returns:
        True: if object is an instance of a class
        False: If object is not an instance of a class

    """
    return isinstance(obj, a_class)
