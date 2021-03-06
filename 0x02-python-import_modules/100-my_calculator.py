#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    ac = len(sys.argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print(f"{a} + {b} =", add(a, b))
        exit(0)

    if operator == '-':
        print(f"{a} - {b} =", sub(a, b))
        exit(0)

    if operator == '*':
        print(f"{a} * {b} =", mul(a, b))
        exit(0)

    if operator == '/':
        print(f"{a} / {b} =", div(a, b))
        exit(0)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
