#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

try:
    my_rectangle.width = "10"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    my_rectangle.height = -3
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
