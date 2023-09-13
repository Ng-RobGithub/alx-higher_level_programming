#!/usr/bin/python3
"""Defines a JSON file-writing function."""
mport json

def save_to_json_file(my_obj, filename):
    """Save a Python object to a text file in JSON format."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
