#!/usr/bin/python3
# function that removes all characters C and c from string


def no_c(my_string):
    new_str = ''
    for i in range(len(my_string)):
        if my_string[i] != 'c' or my_string[i] != 'C':
            new_str += ("{:s}".format(my_string[i]))
    return new_str
