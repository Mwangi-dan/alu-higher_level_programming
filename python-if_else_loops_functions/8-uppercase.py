#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 97:
            if i == range(len(str)):
                 print("{}".format(str[i]), end='\n')
            else:
                 print("{}".format(str[i]), end="")
        else:
            j = ord(str[i]) - 32
            if i == range(len(str)):
                print("{}".format(chr(j)), end='\n')
            else:
                print("{}".format(chr(j)), end="")
