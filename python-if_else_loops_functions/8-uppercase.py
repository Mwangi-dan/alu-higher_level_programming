#!/usr/bin/python3
def uppercase(str):
    ntxt = ""
    for i in (str):
        ch = ord(i)
        if ch >= ord("a") and ch <= ord("z"):
            ch -= 32
            ntxt = chr(ch)
        else:
            ntxt = i
        print("{:s}".format(ntxt), end ="")
    print("")
