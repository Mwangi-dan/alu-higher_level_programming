#!/usr/bin/python3
# Finds all multiples of 2


def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for i in my_list:
            if i % 2 == 0:
                new_list += True
            else:
                new_list += False
        return new_list
    return None
