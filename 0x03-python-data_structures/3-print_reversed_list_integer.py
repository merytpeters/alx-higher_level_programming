#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for num in range(len(my_list)):
        if isinstance(my_list, list):
            print("{:d}" .format(my_list[num]))
