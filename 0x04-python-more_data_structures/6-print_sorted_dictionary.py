#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for c in sorted(a_dictionary.key()):
        print ("{}: {}".format(c, a_dictionary[c])
