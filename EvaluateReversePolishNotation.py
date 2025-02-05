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

for i in tokens:
    
    if i == "+":
        stack.append(stack.pop() + stack.pop())
    
    elif i =="-":
        second, first = stack.pop(), stack.pop()
        stack.append(first - second)
    
    elif i == "*":
        stack.append(stack.pop() * stack.pop())
    
    elif i == "/":
        second, first = stack.pop(), stack.pop()
        stack.append(int(first / second))

    else: 
        stack.append(int(i))

print(stack[0])        