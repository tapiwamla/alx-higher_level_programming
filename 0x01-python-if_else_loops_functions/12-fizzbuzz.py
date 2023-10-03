#!/usr/bin/python3
def fizzbuzz():
    for numeric in range(1, 101):
        if numeric % 3 == 0 and numeric % 5 == 0:
            print('FizzBuzz ', end='')
        elif numeric % 3 == 0:
            print('Fizz ', end='')
        elif numeric % 5 == 0:
            print('Buzz ', end='')
        else:
            print('{} '.format(numeric), end='')
