#!/usr/bin/python3
"""Module for class of a rectangle

"""


class Rectangle():
    """Simple Rectangle class

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle

    """

    def __init__(self, width=0, height=0):
        """Instantiation of sides of rectangle

        Args:
            width (int): width of rectangle
            height(int): height of rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """__width getter

        Returns:
            __width (int): width of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): width of rectangle

        Attrbutes:
            __width (int): width of rectangle

        Raises:
            TypeError: if value os not integer
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def height(self):
        """__height getter

        Returns:
            __height (int): height of rectangle

        """
        return self.__width

    @height.setter
    def height(self, value):
        """Args:
            value (int): height of rectangle

        Attrbutes:
            __height (int): height of rectangle

        Raises:
            TypeError: if value os not integer
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
