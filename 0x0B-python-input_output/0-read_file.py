#!/usr/bin/python3
""" module."""

def read_file(filename=""):
    """read_file"""
    with open(filename, "r", encoding="UTF-8") as f:
    print(f.read(), end="")
