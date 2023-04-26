#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    
    @property
    def size(self):
        """ Getter """
        return self.width