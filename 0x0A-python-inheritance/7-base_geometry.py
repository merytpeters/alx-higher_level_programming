#!/usr/bin/python3
"""Empty Class File"""


class BaseGeometry:
    """Empty BaseGeometry Class"""

    def area(self):
        """Public instance method of the class that raises an error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
