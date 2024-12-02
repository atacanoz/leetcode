from typing import List

strs = ["neet","code","love","you"]

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encoding each string separately with an additional escape for the delimiter to handle empty strings
        return "?{$#|1".join(strs) + "?{$#|1" if strs == [""] else "?{$#|1".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "?{$#|1":  # This is the encoded version of [""] with our delimiter
            return [""]
        return s.split("?{$#|1") if s else []





# str = "?{$#|1".join(strs)    
    
# print(strs)
# s = str.split("?{$#|1")
# print(s)

# s = []

# print(s)
# print(len(s))
# x = "?{$#|1".join(s)   
# print(x)        
# print(list(x))
# print(len(x))

# print("---------------")

# y = x.split("?{$#|1")
# print(y)
# print(len(y))
