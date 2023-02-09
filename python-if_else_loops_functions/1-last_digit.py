#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = number
num_str = str(num)
last_num = num_str[-1]
last_digit_unsigned = int(last_num)
if number < 0:
    last_digit_unsigned = -abs(last_digit_unsigned)
x = last_digit_unsigned
if x > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, x))
elif x < 6 and (x != 0):
    print(f"Last digit of {number:d} is {x:d} and is less than 6 and not 0")
