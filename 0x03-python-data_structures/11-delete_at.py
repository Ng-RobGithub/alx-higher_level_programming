#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        new_list = []
        for i, item in enumerate(my_list):
            if i != idx:
                new_list.append(item)
                return (new_list)
            return (my_list)
