#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        quotient = None
        pass
    finally:
        print("Inside result : {}".format(quotient), end="")
    print()
    return quotient
