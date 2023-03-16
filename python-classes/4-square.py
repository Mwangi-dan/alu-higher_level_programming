#!/usr/bin/python3
"""Module for class Square

"""


class Square:
    """Square Class

    This is a square class

    """

    def __init__(self, size=0):
        """__init__

        The __init__ methid initialies the size value of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.

        Raises:
            TypeError: If `size` type is not `int`
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area

        """
        return self.__size ** 2

    @property
    def __get_size(self):
        """
        Retrieves the size
        
        """
        return self.__size

    @size.setter
    def __set_x(self, size):
        """
        Sets the value of size

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
