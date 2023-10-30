#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Rectangle Class.
        """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Init method.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Width getter.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Return the area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Return the perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
            Print the rectangle with the character #.
            """
        if self.__width == 0 or self.__height == 0:
            return ""
        sy = str(self.print_symbol)
        return ((sy*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """
            Return a string representation of the rectangle.
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
            Print message when instances deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
