#!/usr/bin/python3
# function that replaces all occurrences of an element in new list


def search_replace(my_list, search, replace):
    my_list = list(map(lambda x: replace if x == search else x, my_list))
    return my_list
