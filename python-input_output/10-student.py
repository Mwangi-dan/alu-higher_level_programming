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

    def to_json(self, attrs=None):
        """
        Method that returns directory description
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            res = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] = satr:
                        res[satr] = obj[satr]
            return res
        return obj
