#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dir_new = a_dictionary.copy()
    list_keys = list(dir_new.keys())

    for i in list_keys:
        dir_new[i] *= 2

    return (dir_new)
