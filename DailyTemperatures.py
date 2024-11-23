# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

temperatues = [73, 74, 75, 71, 69, 72, 76, 73]

answer = []
count = 0
for i in range(len(temperatues)):
    for k in range(i + 1, len(temperatues)):
        if temperatues[k]>temperatues[i]:
            print(f"{temperatues[i]} , {temperatues[k]} , {k-i}" ,end = " ")
            break
        print("h")
    print("")
