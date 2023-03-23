#!/usr/bin/python3
"""
Module with function to append string to a file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): name of file
        text (str): text to append

    """
    with open(filename, 'a', encoding='utf-8'):
        return f.write(text)
