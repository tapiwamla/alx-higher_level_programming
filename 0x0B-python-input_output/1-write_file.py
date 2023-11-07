#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
