#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        if (a or b == 0) and (a == 0 and b == 0):
            quotient = None
        elif (a < 0 or b < 0):
            quotient = quotient * -1
    finally:
        print("Inside result : {}".format(quotient), end="")
    print()
    return quotient
