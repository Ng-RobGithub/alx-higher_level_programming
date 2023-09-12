#!/usr/bin/python3
"""Defines an inherited class-checking function."""
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited from a_class.

    Args:
    - obj: The object to check.
    - a_class: The class to check inheritance from.

    Returns:
    - True if obj is an instance of a class inherited from a_class, otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
