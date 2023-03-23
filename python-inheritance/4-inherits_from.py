#!/usr/bin/python3
"""
Module to check if object is an instance of class that inherited
"""


def inherits_from(obj, a_class):
    """
    Function to check if `obj` is a subclass of `a_class`

    Args:
        obj (any): The object to compare
        a_class (class): Class to comapre with object

    Returns:
       `True`: if `obj` is a subclass of `a_class`
       `False`: if `obj` is not a subclass of `a_class`

    """
    return isinstance(obj, a_class)
