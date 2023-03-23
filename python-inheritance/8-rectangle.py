#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module for rectangle class
"""

class Rectangle(BaseGeometry):
    """
    Rectangle Class that inherits from BaseGeometry

    Args:
        BaseGeometry (class)
    """
    def __init__(self, width, height):
        """
        Initialization function

        Args:
            width (int): horizontal dimension of rectangle
            height (int): vertical dimension of rectangle

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
