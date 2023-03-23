#!/usr/bin/python3
"""
Function reads text and prints to stdout
"""


def read_file(filename=""):
    """
    function to open filename and print its contents
    
    Args:
        filename (string): name of file
    
    """
    with open('filename' 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
