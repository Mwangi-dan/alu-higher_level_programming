#!/usr/bin/python3
"""
Module with function to write string to file
"""


def write_file(filename="", text=""):
    """
    Args:
        Filename (string): name of file
        text (str): string to be written to filr

    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
