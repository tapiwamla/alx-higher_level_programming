#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square class defined by geometric shape

        Attributes:
            size (int): Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square object.
        
        Args:
            size (int): Size of a side of the square.
            position (tuple): Position of the square in 2D space.
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area (int).
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): Size of a side of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints a square of the specified size using '#' characters.

        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(0, self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def position(self):
        """
        Getter for the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): Position of the square in 2D space.
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
