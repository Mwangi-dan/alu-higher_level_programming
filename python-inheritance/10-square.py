#!/usr/bin/python3
"""
Square class that inherits from rectangle
and BaseGeometry

"""
Rectangle = __import__('9-rectangle.py').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """Square class that inherits rectangle

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size(self)

    def area(self):
        return self.__size ** 2
