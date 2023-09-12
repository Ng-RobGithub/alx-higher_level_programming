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
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False

# Example usage:
class BaseClass:
    pass

class ChildClass(BaseClass):
    pass

obj = ChildClass()

print(inherits_from(obj, BaseClass))  # True, as obj is an instance of ChildClass, which inherited from BaseClass
print(inherits_from(obj, object))      # True, as all classes inherit from the object class
print(inherits_from(obj, int))         # False, as obj is not an instance of int
