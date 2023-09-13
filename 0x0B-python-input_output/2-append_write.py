#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8) and return the number of characters added."""

    with open(filename, mode='a', encoding='utf-8') as file:
        char_count = file.write(text)
        return (char_count)
