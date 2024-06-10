#!/usr/bin/python3
"""Returns a function lookup()"""


def lookup(obj):
    """Function that returns a list of available attributes and methods
    of an object
    Returns:
        list: list of available attributes and methods of an object
    """

    return dir(obj)
