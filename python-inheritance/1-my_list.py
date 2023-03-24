#!/usr/bin/python3
"""
MyList class that inherits list class

Argv:
    List: (class)
"""


class MyList(list):
    """My List Class"""

    def print_sorted(self):
        """
        Prints a list in ascending order
      
        Sorts list then prints it
        """
        if issubclass(MyList, list):
            print(sorted(self))
