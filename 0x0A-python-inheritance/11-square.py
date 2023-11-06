#!/usr/bin/python3
"""
Square Module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class.
    """
    def __init__(self, size):
        """
        Initialize the square base on rectangle.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Define area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
