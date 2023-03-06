#!/usr/bin/python3
# function returns tuple with the length of a string and first character


def multiple_returns(sentence):
    lng = len(sentence)
    if len(sentence) == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return lng, f_char
