#!/usr/bin/python3
"""lookup module"""


class MyList(list):
    """custom MyList class"""
    def print_sorted(self):
        """ method for printing"""
        print(sorted(self))
