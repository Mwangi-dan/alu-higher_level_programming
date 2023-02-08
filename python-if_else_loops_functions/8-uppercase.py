#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 97:
            print(str[i], end="")
        else:
            j = ord(str[i]) - 32
            print(chr(j), end="")
