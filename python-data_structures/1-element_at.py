#!/usr/bin/python3
# script to access element at a particlar point in list


def element_at(my_list, idx):
    if (idx < 0):
        return None
    elif (idx > len(my_list)):
        return None
    else:
        return (my_list[idx])
