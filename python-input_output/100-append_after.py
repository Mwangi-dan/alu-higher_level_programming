#!/usr/bin/python3
"""
Module that inserts line of text after specific sstring
"""


def append_after(filename="", search_string="", new_string=''):
    """ Function that inserts a line of text to a file
     after each line containing a specific dtring
     """
    with open(filename, r+, encoding="utf8") as f:
        all_text = f.readlines()
        new_text = ""
        for line in all_text:
            new_text += line
            if search_string inline:
                new_text += new_string

        f.seek(0)
        f.write(new_text)
