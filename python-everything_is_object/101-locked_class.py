#!/usr/bin/python3
"""
Defines a Locked Class
"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """
    __slots__ = ["first_name"]
