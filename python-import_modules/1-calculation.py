#!/usr/bin/python3
# script to import calculation functions and do operations on numbers

if __name__ == "__main__":
    import calculator_1
    # assigning shorter names to the imported functions
    add = calculator_1.add
    sub = calculator_1.sub
    mul = calculator_1.mul
    div = calculator_1.div
    # initializing variables
    a = 10
    b = 5
    # printing the operations
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
