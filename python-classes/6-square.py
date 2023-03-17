#!/usr/bin/python3
"""Module for Sqaure class

"""


class Square:
    """Square Class

    This is a square class

    Args:
        size (int): length of one side of square
        position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines

    Attributes:
        __size (int): length of one side of square
        __position (tuple) ((int), (int)): horizonatal offset in spaces,
        vertical offset in newlines

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initialies the size value of the square.

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
        self.position = position

    def area(self):
        """
        Returns the current square area

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size

        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the value of size

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Prints text representation of square in hash chars,
        horizontally and vertically offset by first and second int
        in __position, respectively.

        Attributes:
            __size (int): length of one side of square
            __position (tuplr) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
        if self.__size == 0:
            print()
            return None
        for v_offset in range(0, self.__position[1]):
            print()
        for row in range(0, self.__size):
            for h_offset in range(0, self.__position[0]):
                print(" ", end="")
            for col in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """___position getter, setter with some method name

        Returns:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (int): tuple of two positive integers

        Attributes:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in values

        Raises:
            TypeError: if value is not a tuple of two positive ints

        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                                '2 positive integers')

        self.__position = value
