#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None or key not in a_dictionary:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
