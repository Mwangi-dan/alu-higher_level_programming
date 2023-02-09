#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    num_str = str(number)
    last_digit_unsigned = int(num_str[-1])
    return -last_digit_unsigned if (number < 0) else last_digit_unsigned
x = last_digit(number)
s = "Last digit of "
if x > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, x))
elif x < 6 and (x != 0):
    print(f"{:s}{number:d} is {x:d} and is less than 6 and not 0")
