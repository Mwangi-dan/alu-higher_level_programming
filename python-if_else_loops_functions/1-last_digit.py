#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_string = str(number)
num_last = num_string[-1]
if int(num_last) > 5:
    print(f"Last digit of {number} is {num_last} and is greater than 5 and not 0")
elif int(num_last) == 0:
    print(f"Last digit of {number} is {num_last} and is 0")
elif int(num_last) > 5 and num_last != 0:
    print(f"Last digit of {number} is {num_last} and is less than 6 and not 0")
