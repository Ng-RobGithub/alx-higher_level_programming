#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """Get the list of attributes and methods of the object"""

    attributes_and_methods = dir(obj)
    return (attributes_and_methods)
