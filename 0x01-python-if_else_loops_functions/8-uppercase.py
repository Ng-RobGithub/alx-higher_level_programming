#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
            print("{:c}".format(ord(char)), end="")
            print()  # Print a newline
