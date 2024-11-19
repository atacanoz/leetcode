# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

import re
from math import trunc

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = []

for i in range(len(tokens)):
    match = re.search(r'\b-?\d+\b', tokens[i])
    if bool(match):
        stack.append(int(tokens[i]))
    elif tokens[i] == "+":
        temp = stack.pop()
        temp = temp + stack.pop()
        stack.append(temp)
    elif tokens[i] == "-":
        temp = stack.pop()
        temp = stack.pop() - temp 
        stack.append(temp)     
    elif tokens[i] == "*":
        temp = stack.pop()
        temp = temp * stack.pop()
        stack.append(temp)

    elif tokens[i] == "/":
        temp = stack.pop() 
        temp = stack.pop() / temp
        stack.append(int(temp))
    print(stack)



# x= 6 / -132

# print(x)

# print(int(x))
