#!/usr/bin/python3
"""File that contrains a function"""


def is_same_class(obj, a_class):
    """Function that returns true if the obj is exactly an instance
    of the specified class"""

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
