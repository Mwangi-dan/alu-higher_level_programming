#!/usr/bin/python3

"""
Square class that inherits rectangle
and BaseGeometry

Args
    Square (class): Class for square

"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square class that inherits rectangle class

    Args
        Rectangle (class)
    """
    def __init__(self, size):
        """
        Initializes size of square

        Args
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
        """
        return self.__size ** 2
