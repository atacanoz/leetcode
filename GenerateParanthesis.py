# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# only add open paranthesis if open < n
# only add a closing paranthesis if open > closed 
# valid until open == closed == n


def generateParenthesis(n: int):
    stack = []
    res = []

    def backtrack(open, closed):
        if open == closed == n:
            res.append("".join(stack))
            return 
        if open < n:
            stack.append("(")
            backtrack(open + 1, closed)
            stack.pop()
        if open > closed:
            stack.append(")")
            backtrack(open, closed + 1)
            stack.pop()

    backtrack(0,0)
    return res

   
n = 5

print(generateParenthesis(n))
