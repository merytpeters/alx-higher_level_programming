#!/usr/bin/python3
"""Contains a function"""


def inherits_from(obj, a_class):
    """Returns true if the obj is an instance of a class that inherited
    (directly or indirectly) from the specified class"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
