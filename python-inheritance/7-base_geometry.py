#!/usr/bin/python3
"""
Base Geometry class
"""


class BaseGeometry:
    """
    Raises exception

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer

        Returns:
            TypeError: If value is not an integer
            ValueErroe: If value is less than or equal to 0

        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
