import heapq

nums = [0,3,7,2,5,8,4,6,0,1]

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


heapq.heapify(nums)
print(nums)
longest_count = 1
count = 1


while nums:

    x = heapq.heappop(nums)
    if nums:
        front = nums[0]
        if front == (x + 1):
            count+=1
        else:
            if count > longest_count:
                longest_count = count
            count=1
    else:
        if count > longest_count:
            longest_count = count     
                
                   

print(longest_count)
 
        

    