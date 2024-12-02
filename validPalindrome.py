# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
print(s)

newstr = ""

for c in s:
    if c.isalnum():
        newstr += c.lower()

print(newstr)        

if newstr == newstr[::-1]: #checking with reverse of the newstr 
    print("true")  
else:
    print("false")    
         
