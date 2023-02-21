#!/usr/bin/python3
# script that impirts function from another file
if __name__ == "__main__":
    import add_0 as add
    sum = add.add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, sum(a, b)))
