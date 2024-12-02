
nums = [100,4,200,1,3,2]

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

longest, count = 0, 0 
x = set(nums)

for n in x:
    if n-1 not in x:
        count = 1
        print(f"begining of seq: {n}")
        while n+1 in x:
            n+=1
            count+=1
        if count > longest:
            longest = count    
            

print(longest)
       





