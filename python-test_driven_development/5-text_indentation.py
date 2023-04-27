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

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
