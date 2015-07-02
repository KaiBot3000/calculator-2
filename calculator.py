"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# while loop that's true
while True:
    # take input and evaluate
    input = raw_input("Type a math equation! >")
    # split up values into a list
    tokens = input.split(" ") #tokens should be a list
    # tokens = ["*", "4", '3']
    # check list length

        # if input length == 1
            if len(tokens) == 1:
                if tokens[0] == 'q':
                    break
                else:
                    pass error()    
        # if input length == 2
            if len(tokens) == 2:
                int1 = tokens[1]
            # do int1
                if tokens[0] == "square":
                    print square(int1)
                elif tokens[0] == "cube":
                    print cube(int1) 
                else:
                    pass error()
        # if input length == 3
            if len(tokens) == 3:
                int1 = tokens[1]
                int2 = tokens[2]
            # do int1, int2
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

                elif tokens[0] == "pow":
                    print power(int1, int2)

                elif tokens[0] == "mod":
                    print mod(int1, int2)
                else:
                    pass error()



