# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
print(s)
s_alnum = ""
s_check = ""
stack = []

for c in s:
    if c.isalnum():
        s_alnum += c.lower()
        stack.append(c.lower())

while stack:
    s_check += stack.pop()


if s_check == s_alnum:
    print("TRUE")
else: 
    print("FALSE")    


         
