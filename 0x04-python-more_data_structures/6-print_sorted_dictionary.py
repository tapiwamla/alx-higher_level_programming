#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = list(a_dictionary.keys())
    ord_list.sort()

    for index in ord_list:
        print("{}: {}".format(index, a_dictionary.get(index)))
