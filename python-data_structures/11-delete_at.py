#!/usr/bin/python3
# function that deletes element at specific position of list


def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):

