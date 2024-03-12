#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = int(number % 10) #variable that stores the last digit
if number < 0:
    last_digit *= int(-1)
    if last_digit < 0:
        print(f"{str} {number:d} is {last_digit:d} and is less than 6 and not 0")
    elif last_digit == 0:
            print(f"{str} {number:d} is {last_digit:d} and is 0")
elif number > 0:
    if last_digit > 5:
        print(f"{str} {number:d} is {last_digit:d} and is greater than 5")
    elif last_digit < 6:
        print(f"{str} {number:d} is {last_digit:d} and is less than 6 and not 0")
    elif last_digit == 0:
        print(f"{str} {number:d} is {last_digit:d} and is 0")
elif number == 0:
    printf(f"{str} {number:d} is {last_digit:d} and is 0")
else:
    print("Error! not a digit")
