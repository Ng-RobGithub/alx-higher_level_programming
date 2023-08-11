#!/usr/bin/python3
def uppercase(s):
    for char in s:
        char_code = ord(char)
        if 97 <= char_code <= 122:  # ASCII range for lowercase letters
            char_code -= 32  # Convert to uppercase ASCII
            print("{:c}".format(char_code), end="")

            print()
