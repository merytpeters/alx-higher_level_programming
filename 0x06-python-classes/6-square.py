#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """This class represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        if isinstance(size, int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) or isinstance(value, int) or len(value) == 2:
            if all(i > 0 for i in value):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        return self.__size ** 2
    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__position[1] > 0):
            print()
        for i in range(self.__size):
            print("#" * self.__size + " " * self.__position[0])
