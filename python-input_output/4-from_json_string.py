#!/usr/bin/python3
"""
Module with function that returns string from JSON representation
"""
import json


def from_json_string(my_str):
    """
    function to return object from JSON representation

    Args:
        my_obj
    """
    return json.loads(my_str)
