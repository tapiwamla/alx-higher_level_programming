#!/usr/bin/python3
""" A module for square. """


class Square:
    """
    The square class defined.

        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0):
        """
        Initializes the square
        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.__size = size

    def area(self):
        """
        Set square area.

        Return:
            The current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter.

        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter.

        Args:
            size (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value
