#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(vaue))
        return True
    except (ValueError, TypeError):
        return false
