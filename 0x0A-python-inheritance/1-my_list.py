#!/usr/bin/python3
"""
Module inherit list.
"""


class MyList(list):
    """
    MyList
    """
    def print_sorted(self):
        """
        Print a sorted List
        """
        print(sorted(self))
