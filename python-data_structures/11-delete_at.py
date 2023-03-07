#!/usr/bin/python3
# function that deletes element at specific position of list


def delete_at(my_list=[], idx=0):
    if 0 <= len(my_list) > idx:
        del my_list[idx]
    return my_list
