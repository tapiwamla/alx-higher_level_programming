#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
my_digit = abs(number) % 10
if number < 0:
    my_digit = -my_digit

response = f'Last digit of {number} is {my_digit} and is '

if my_digit > 5:
    response += 'greater than 5'
elif my_digit == 0:
    response += '0'
else:
    response += 'less than 6 and not 0'

print(response)
