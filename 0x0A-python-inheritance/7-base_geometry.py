#!/usr/bin/python3
"""lookup module"""


class BaseGeometry:
    """basegeometry class """
    def area(self):
        """ method to compute the area"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """ integer_validator """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
