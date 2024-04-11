#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = 0
    try:
        quotient = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        if (a or b) == 0 and (a and b) == 0:
            quotient = None
            pass
    finally:
        print("Inside result : {}".format(quotient), end="")
        if (a or b) < 0:
            quotient = quotient * -1
    print()
    return quotient
