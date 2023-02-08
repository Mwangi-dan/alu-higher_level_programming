#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    num_str = str(number)
    last_digit_unsigned = int(num_str[-1])
    return -last_digit_unsigned if (number < 0) else last_digit_unsigned
x = last_digit(number)
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif x == 0:
    print(f"Last digit of {number} is {x} and is 0")
elif x < 6 and (x != 0):
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
