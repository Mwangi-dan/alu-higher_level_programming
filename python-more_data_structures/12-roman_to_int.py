#!/usr/bin/python3


def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    pre = 0
    res = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if val[roman_string[i]] < p:
            res += val[roman_string[i]]
        else:
            res -= val[roman_string[i]]
        prev = val[roman_string[i]]
    print(res)
