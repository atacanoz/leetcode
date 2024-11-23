# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

answer = []

for i in range(len(temperatures)):
    count = 0
    for k in range(i + 1, len(temperatures)):    
        count += 1        
        if temperatures[k] > temperatures[i]:
            break
    else: 
        count = 0           
        
        
    # print(f"{temperatures[i]} , {temperatures[k]} , {i}, {k}" ,end = " ")    
    # print("")
    answer.append(count)

print(answer)
