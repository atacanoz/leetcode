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

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
res = list()

# [-4, -1, -1, 0, 1, 2]



for i in range(len(nums)-2):
    if nums[i] == nums[i-1]:
        continue
    j = i + 1
    k = len(nums)-1 

    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total > 0:
            k-=1
        elif total < 0:
            j+=1
        else:
            triplet = [nums[i],nums[j],nums[k]]   
            res.append(triplet)
            j+=1
       
                
print(res)

