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
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            print()
        elif text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print(text[i], end="")
