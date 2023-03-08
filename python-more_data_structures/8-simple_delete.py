#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    return a_dictionary.pop(key) if key not in a_dictionary else a_dictionary
