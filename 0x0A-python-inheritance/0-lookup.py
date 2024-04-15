#!/usr/bin/python3
"""Returns a function lookup()"""

def lookup(obj):
    """Returns a list of available attributes and methods of an obj

       Returns:
           list: list of available attributes and methods of an object
    """
    return dir(obj)
