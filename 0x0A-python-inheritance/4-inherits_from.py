#!/usr/bin/python3
"""lookup module"""


def inherits_from(obj, a_class):
    """ if the class inherts from object instance"""
    return isinstance(obj, a_class) and type(obj) != a_class
