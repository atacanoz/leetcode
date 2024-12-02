# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it can trap after raining.


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

area , i , j = 0 , 0 , len(height) - 1 


while i<j and height[i] <= height[i+1]:
    i+=1    

while i<j and height[j] <= height[j-1]:
    j-=1

while i < j:
    if height[j] > height[i]:
        if height[i] > height[i+1]:
            area += height[i] - height[i+1]
            height[i+1]= height[i]
        i+=1
        
    else:
        if height[j] > height[j-1]:
            area += height[j]-height[j-1]
            height[j-1]=height[j]
        j-=1
           
print(area)
    



    


