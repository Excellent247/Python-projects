# argument from command line
# command : python calculator.py 5 add 6

import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    minus = num1 - num2
    return minus

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "plus":
    output = addition(num1, num2)
    print(output)
elif operation == "minus":
    output = sub(num1, num2)
    print(output)