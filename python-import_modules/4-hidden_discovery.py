#!/usr/bin/python3
# Script that prints all names defines by the compiled module

import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print("{}".format(i))
