#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    sorted_keys = sorted(a_dictionary)
    a_dictionary[key] = value
    return a_dictionary
