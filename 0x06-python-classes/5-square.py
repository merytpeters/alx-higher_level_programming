#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """This class represents a square."""
    def __init__(self, size=0):
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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size > 0):
            for i in range(self.__size):
                print('#' * self.__size)
        elif (self.__size == 0):
            print()
