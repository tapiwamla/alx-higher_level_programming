#!/usr/bin/python3
def number_keys(a_dictionary):
    my_number = 0
    list_keys = list(a_dictionary.keys())

    for index in list_keys:
        my_number += 1

    return (my_number)
