#!/usr/bin/python3
"""A module of a class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Gets the height"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
