#!/usr/bin/python3
'''
Module to check if objects are from specified class

'''


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is an instance of a class
    Checks if `obj` is an instance if a lass this inherited from

    Args:
        obj: (any): Object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if the object is exactly an instance of specifies class;
        otherwise `False`

    """
    return isinstance(obj, a_class)
