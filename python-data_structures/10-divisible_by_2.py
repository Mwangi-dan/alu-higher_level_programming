#!/usr/bin/python3
# Finds all multiples of 2


def divisible_by_2(my_list=[]):
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                i = True
            else:
                i = False
    return None
