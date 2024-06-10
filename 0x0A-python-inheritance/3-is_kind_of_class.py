#!/usr/bin/python3
"""File that contains a function"""


def is_kind_of_class(obj, a_class):
    """Returns true if te obj is an instance of or the obj is an
    instance of a class that inherited from the specified class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
