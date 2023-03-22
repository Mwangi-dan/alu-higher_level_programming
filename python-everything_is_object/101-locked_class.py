#!/usr/bin/python3
"""Locked Class
This class has no class or object attribute that prevents
user from dynamically creating new instance attributes

Args:
    first_name: (str) Takes in the name

"""

class LockedClass:
    if __name__ == "__first_name__":
       def first_name(self, name):
           self.name = name
