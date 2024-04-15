#!/usr/bin/python3
"""Returns a function lookup()"""

def lookup(obj):
    """Returns a list of available attributes and methods of an obj"""
    return dir(obj)
