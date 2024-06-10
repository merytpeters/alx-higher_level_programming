#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """"Inheritance of list"""

    def print_sorted(self):
        """Public instance method that prints the list and sort in
        ascending order"""
        print(sorted(self))
