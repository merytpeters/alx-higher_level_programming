#!/usr/bin/python3
def no_c(my_string):
    charList = list(my_string)
    for char in my_string:
        if char == 'c' or char == 'C':
            charList.remove(char)
            my_string = ''.join(charList)
    return (my_string)
