#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Read and print the contents of a text file to stdout."""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
