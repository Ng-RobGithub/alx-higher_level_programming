#!/usr/bin/python3
def swap(a, b):
    a, b = b, a
    return (a, b)

a = 89
b = 10
a, b = swap(a, b)
print("a={:d} - b={:d}".format(a, b))
