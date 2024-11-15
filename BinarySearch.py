# Given an array of integers nums which is sorted in ascending order, and an integer target
# Write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


nums = [0,1,2,3,4,5,6,7,8,9,10,11,12]
target = 6

left , right = 0, len(nums)-1
mid = (left + right) // 2

while nums[mid] != target:
    if nums[mid] > target:
        right = mid
        mid = mid // 2
    else:
        left = mid 
        mid = (mid + right)//2    
    print(left, mid,right)
    



print(mid)
