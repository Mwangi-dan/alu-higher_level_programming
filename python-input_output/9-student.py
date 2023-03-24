#!/usr/bin/python3
"""
Module with class student
"""


class Student:
    """
    Class defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization methid
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that returns directory description
        """
        res = {}
        if hasattr(self, "__dict__"):
            res = self.__dict__.copy()
        return res
