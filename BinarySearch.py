# Given an array of integers nums which is sorted in ascending order, and an integer target
# Write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

#        0  1  2  3  4  5  6
nums = [-1, 0, 5] 
target = 9
s = len(nums)

i = s//2

for j in range(s//2):
    if nums[i] < target:
        i = (s + i)//2
 
    else:
        i = (s - i) //2


if target not in nums:
    i = -1

print(i)        
            

    


# x += (len(nums)-x) // 2

# print(x)

# x += (len(nums)-x) // 2

