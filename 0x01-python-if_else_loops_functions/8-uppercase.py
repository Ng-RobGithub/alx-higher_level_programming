#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            diff = ord('A') - ord('a')
            uppercase_char = chr(ord(char) + diff)
            print("{:c}".format(ord(uppercase_char)), end="")
        else:
            print("{:c}".format(ord(char)), end="")

            print()
