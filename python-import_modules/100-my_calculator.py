#!/usr/bin/python3
# Calculator with function from inported module
import sys

if __name__ == "__main__":
    import calculator_1
    a = len(sys.argv) - 1
    if a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    add = calc.add
    sub = calc.sub
    div = calc.div
    mul = calc.mul

    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[3])

    if op == "+":
        print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
        sys.exit(0)
    elif op == "-":
        print(f"{num_1} - {num_2} = {sub(num_1, num_2)}")
        sys.exit(0)
    elif op == "*":
        print(f"{num_1} * {num_2} = {mul(num_1, num_2)}")
        sys.exit(0)
    else:
        print(f"{num_1} / {num_2} = {div(num_1, num_2)}")
        sys.exit(0)
