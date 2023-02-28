#!/usr/bin/python3
# replaces an element in list at specific position without modifying


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for i in range(len(new_list)):
            if i == idx:
                new_list[i] = element
        return new_list
