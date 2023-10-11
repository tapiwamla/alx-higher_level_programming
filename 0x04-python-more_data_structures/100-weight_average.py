#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    my_number = 0
    my_denominator = 0

    for my_tuple in my_list:
        my_number += my_tuple[0] * my_tuple[1]
        my_denominator += my_tuple[1]

    return (my_number / my_denominator)
