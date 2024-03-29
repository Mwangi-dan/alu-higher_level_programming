#!/usr/bin/python3
"""Module for class of a rectangle

"""


class Rectangle():
    """Simple Rectangle class

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments number of instances,
        Instantiation of sides of rectangle

        Args:
            width (int): width of rectangle
            height(int): height of rectangle

        """
        type(self).number_of_instances += 1

        self.width = width
        self.height = height

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
        self.__width = value

    @property
    def height(self):
        """__height getter

        Returns:
            __height (int): height of rectangle

        """
        return self.__height

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

    def area(self):
        """Returns:
            Area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns:
            Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangke
        representes by the current instance.

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle
            str (str): constructed for retunr

        Returns:
            str (str): string suitable for printing rectangle

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '{}'.format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """For direct printing of instancees

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """printts message upon deletion of rectangle

        """
        cls.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two

        Args:
            rect_1: first instance
            rect_2: second instance

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
