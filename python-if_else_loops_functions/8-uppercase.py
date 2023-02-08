#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 97:
            print("{}".format(str[i]), end='')
        else:
            j = ord(str[i]) - 32
            print("{}".format(chr(j)), end="")
