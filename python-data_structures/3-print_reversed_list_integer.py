#!/usr/bin/python3
# script that reverses integers in list

def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for i in range(len(rev_list) - 1):
        print("{:d}".format(rev_list[i]))
