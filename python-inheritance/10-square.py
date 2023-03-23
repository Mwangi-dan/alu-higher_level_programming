#!/usr/bin/python3
"""
Imports classes from Rectangle and BaseGeometry

"""
Rectangle = __import__('9-rectangle.py').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Square class that inherits from rectangle
and BaseGeometry

Args:
    Square (class): Class for square derived from rectangle

"""

class Square(Rectangle):
    """Square class that inherits rectangle

    """
    def __init__(self, size):
        """
        Initializes size of square

        Args:
            size (int): horizontal and vertical dimension of square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size(self)

    def area(self):
        """
        Finds area of square

        Args:
            size (int)
        return self.__size ** 2
