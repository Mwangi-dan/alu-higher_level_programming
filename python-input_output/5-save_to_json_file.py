#!/usr/bin/python3
"""
Module to write an object to a text file, using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj 
        filename (string): name of file
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
