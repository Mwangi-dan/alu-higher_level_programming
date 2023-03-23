#!/usr/bin/python3
"""
Module to create ibject from json file
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (string): name of file
    """
    woth open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
