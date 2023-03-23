#!/usr/bin/python3
"""
Function reads text and prints to stdout
"""


def read_file(filename=""):
    with open('filename' 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
