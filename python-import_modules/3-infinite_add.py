#!/usr/bin/python3
# script to add integer arguments
import sys
a = sys.argv
add = 0
for i in range(1, len(a)):
    num = int(a[i])
    add += num
print(add)
