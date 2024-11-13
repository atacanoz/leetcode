# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

import collections

nums = [-1,0,1,2,-1,-4]

x = collections.defaultdict()

target = int


for i in range(len(nums)):
    j = i + 1
    while len(nums) > j:
        if -nums[i]-nums[j] in nums:
            if nums.index(-nums[i]-nums[j]) != i and nums.index(-nums[i]-nums[j]) != j:
                y = [nums[i], nums[j], -nums[i]-nums[j]]
                x[(nums[i], nums[j], -nums[i]-nums[j])]
           
        j+=1    
      

print(x)