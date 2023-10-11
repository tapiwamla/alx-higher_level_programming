#!/usr/bin/python3

def subtract_notation(list_num):
    to_sub = 0
    list_max = max(list_num)

    for n in list_num:
        if list_max > n:
            to_sub += n

    return (list_max - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_symbols = {'I': 1, 'V': 5, 'D': 500, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
    list_keys = list(rom_symbols.keys())

    my_number = 0
    last_rom = 0
    list_num = [0]

    for chr in roman_string:
        for r_num in list_keys:
            if r_num == chr:
                if rom_symbols.get(chr) <= last_rom:
                    my_number += subtract_notation(list_num)
                    list_num = [rom_symbols.get(chr)]
                else:
                    list_num.append(rom_symbols.get(chr))

                last_rom = rom_symbols.get(chr)

    my_number += subtract_notation(list_num)

    return (my_number)
