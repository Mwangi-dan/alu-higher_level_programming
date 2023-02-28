#!/usr/bin/python3
# replaces an element in list at specific position without modifying


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                my_list[i] = element
