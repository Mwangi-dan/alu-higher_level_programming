#!/usr/bin/python3
"""
Lis and methods of an object
Argvs:
    Obj: class object
Returns:
    List of available attributes and methods of an object
"""
def lookup(obj):
    """
    Lookup function
    """
    return dir(obj)
