#!/usr/bin/python3
# script to import calculation functions and do operations on numbers
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    # initializing variables
    a = 10
    b = 5
    # printing the operations
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
