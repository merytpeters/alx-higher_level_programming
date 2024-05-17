#!/usr/bin/python3
"""An inheritance rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class inheritance"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of attributes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """setter for width"""
        return self.__width

    @property
    def height(self):
        """setter for height"""
        return self.__height

    @property
    def x(self):
        """setter for x"""
        return self.__x

    @property
    def y(self):
        """setter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        else:
            raise ValueError("Width must be a positive integer")

    @height.setter
    def height(self, value):
        """setter for height"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        else:
            raise ValueError("height must be a positive integer")

    @x.setter
    def x(self, value):
        """setter for x"""
        if isinstance(value, int) and value >= 0:
            self.__x = value
        else:
            raise ValueError("x must be a positive integer")

    @y.setter
    def y(self, value):
        """setter for y"""
        if isinstance(value, int) and value >= 0:
            self.__y = value
        else:
            raise ValueError("y must be a positive integer")
