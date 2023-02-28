#!/usr/bin/python3
# replaces an element in list at specific position without modifying


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        if i == idx:
            my_list[i] = element

