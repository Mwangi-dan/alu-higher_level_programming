#!/usr/bin/python3
"""
Module for say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints out first and last name in a string

    :param first_name (string): first name
    :param last_name (string): last name (default is empty string)

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
    