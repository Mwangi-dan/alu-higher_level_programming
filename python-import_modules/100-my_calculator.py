#!/usr/bin/python3
# Calculator with function from inported module
import sys
import calculator_1 as calc

if __name__ == "__main__":
    a = len(sys.argv) - 1
    if a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[3])

    if op == "+":
        print(f"{num_1} + {num_2} = {calc.add(num_1, num_2)}")
        sys.exit(0)
    elif op == "-":
        print(f"{num_1} - {num_2} = {calc.sub(num_1, num_2)}")
        sys.exit(0)
    elif op == "*":
        print(f"{num_1} * {num_2} = {calc.mul(num_1, num_2)}")
        sys.exit(0)
    else:
        print(f"{num_1} / {num_2} = {calc.div(num_1, num_2)}")
        sys.exit(0)
