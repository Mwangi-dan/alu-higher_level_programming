#!/usr/bin/python3
"""
Module with function that returns JSON representation of string
"""
import json


def to_json_string(my_obj):
    """
    function to return JSON representation of object

    Args:
        my_obj
    """
    return json.dumps(my_obj)
