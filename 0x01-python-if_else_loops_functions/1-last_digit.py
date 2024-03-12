#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = abs(number) % 10  '#variable that stores the last digit'
if number < 0:
    last_digit = -(last_digit)
if last_digit > 5:
    print(f"{str} {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"{str} {number:d} is {last_digit:d} and is 0")
elif last_digit < 6:
    print(f"{str} {number:d} is {last_digit:d} and is less than 6 and not 0")
elif number == 0:
    printf(f"The only digit of {number:d} is {last_digit:d}")
else:
    print("Error! not a digit")
