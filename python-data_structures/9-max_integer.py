#!/usr/bin/python3
# finds biggest integer of list


def max_integer(my_list=[]):
    if my_list:
        temp = my_list[0]
        for i in range(len(my_list)):
            if temp < my_list[i]:
                temp = my_list[i]
        return temp if len(my_list) > 0 else None
    return None
