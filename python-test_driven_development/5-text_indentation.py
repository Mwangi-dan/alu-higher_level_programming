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
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        elif text[i] == " " and text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":":
            print(text[i].strip(), end="")
        else:
            print(text[i], end="")
