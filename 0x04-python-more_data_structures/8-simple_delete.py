#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
        print_sorted_dictionary(a_dictionary)
        print("--")
