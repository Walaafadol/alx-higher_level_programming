#!/usr/bin/python3
"""lookup module"""


class BaseGeometry:
    """basegeometry class """
    def area(self):
        """ method to compute the area"""
        raise Exception('area() is not implemented')
