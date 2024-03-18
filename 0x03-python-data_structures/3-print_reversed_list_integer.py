#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversedList = my_list[::-1]
    for num in range(len(reversedList)):
        print("{:d}" .format(reversedList[num]))
