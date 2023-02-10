#!/usr/bin/python3
i = 0
for j in range(ord('z'), ord('a')- 1, -1):
    print("{}".format(chr(j - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
    
