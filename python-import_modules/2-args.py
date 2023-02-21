#!/usr/bin/python3
# script to display number of elements in argv
import sys
if __name__ == "__main__":
    a = sys.argv
    if (len(a) - 1) == 0:
        print("0 arguments.")
    elif (len(a) - 1) == 1:
        print("1 argument:")
    else:
        print(f"{(len(a) - 1):d} arguments:")
    for i in range(1, len(a)):
        print(f"{i:d}: {a[i]}")
