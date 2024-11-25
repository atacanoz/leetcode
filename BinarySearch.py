# Given an array of integers nums which is sorted in ascending order, and an integer target
# Write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


nums = [0,1,2,3,4,5,6,7,8,9,10,11,12]
target = 13

def BinarySearch(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1            

res = BinarySearch(nums, target)

print(res)
