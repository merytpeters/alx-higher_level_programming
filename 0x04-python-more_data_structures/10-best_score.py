#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name = ''
    max_key = float('-inf')
    for student, key in a_dictionary.items():
        if key > max_key:
            name = student
            max_key = key
    return (name)
