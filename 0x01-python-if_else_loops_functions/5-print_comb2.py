#!/usr/bin/python3
for numeric in range(0, 100):
    if numeric == 99:
        print('{}'.format(numeric))
    else:
        print('{:02}'.format(numeric), end=', ')
