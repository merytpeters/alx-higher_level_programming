#!/usr/bin/python3
"""Addition function
Checks for negative and positive infinity float
"""


def add_integer(a, b=98):
    """Adds two integer
    Checks that a and b are integers
    Checks if float is infinity"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    if result == float('inf') or result == -float('inf'):
        raise OverflowError("Result is too large")
    return result
    

