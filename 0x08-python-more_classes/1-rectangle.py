#!/usr/bin/python3
"""A module of a class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height  # Instantion of the class
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if (value >= 0):
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if (value >= 0):
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
