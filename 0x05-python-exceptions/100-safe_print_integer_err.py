#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    intger = True
    try:
        print("{}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        intger = False
    return intger
