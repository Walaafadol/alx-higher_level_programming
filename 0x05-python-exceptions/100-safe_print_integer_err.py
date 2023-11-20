#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    is_int = True
    try:
        print("{}".format(value))
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        is_int = False
    return is_int
