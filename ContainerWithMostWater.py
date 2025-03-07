# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49. 

height = [1,8,6,2,5,4,8,3,7]   

max_area = 0
i = 0
j = len(height)-1

while i < j:

    if height[j] > height[i]:
        area = height[i] * (j - i)
        i+=1

    else:
        area = height[j] * (j - i)
        j-=1
    if area > max_area:
        max_area = area
    
print(max_area)

             