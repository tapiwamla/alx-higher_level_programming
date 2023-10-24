#!/usr/bin/python3
""" The module for square. """


class Square:
    """ The square class defined. """
    def __init__(self, size=0):
        """ Initialize the method. """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
