#!/usr/bin/python3
def uppercase(str):
    for char in str:
        result = char
        if ord(result) >= 97 and ord(result) <= 122:
            result = chr(ord(char) - ord('a') + ord('A'))
        print("{:s}" .format(result), end="")
    print()
