#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json

def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
