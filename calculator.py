"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# while loop that's true
while True:
    # take input and evaluate
    input = raw_input("Type a math equation! >")
    # split up values into a list
    tokens = input.split(" ") #tokens should be a list
    # if q, a quit statement
    if tokens[0] == 'q':
        break
    # run math equation according to list values
    else:
        # need to provide option for just one argument/input/integer
        int1, int2 = int(tokens[1]), int(tokens[2])
        if tokens[0] == "+":
            result = add(int1, int2)
            print result
        elif tokens[0] == "-":
            result = subtract(int1, int2)
            print result

        elif tokens[0] == "*":
            result = multiply(int1, int2)
            print result

        elif tokens[0] == "/":
            print divide(int1, int2)

        elif tokens[0] == "square":
            print square(int1)

        elif tokens[0] == "cube":
            print cube(int1) 

        elif tokens[0] == "pow":
            print power(int1, int2)

        elif tokens[0] == "mod":
            print mod(int1, int2)


