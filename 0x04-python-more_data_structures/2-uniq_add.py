#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    my_number = 0

    for index in uniq_list:
        my_number += index

    return (my_number)
