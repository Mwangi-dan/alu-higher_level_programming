#!/usr/bin/python3
"""
Module containing function for text-indentation

"""


def text_indentation(text):
    """
    Prints a text with 2 new line after ".", "?" and ":"

    :param text (string): text to be printed

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])
