# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

temperatures = [73,74,75,71,69,72,76,73]
answer = [0] * len(temperatures)  # Initialize the result list with zeros
stack = []  # This will store indices of temperatures

for i in range(len(temperatures)):
    # While stack is not empty and current temperature is greater than the temperature at the index on top of the stack
    while stack and temperatures[i] > temperatures[stack[-1]]:
        prev_day = stack.pop()  # Get the index of the previous day
        answer[prev_day] = i - prev_day  # Calculate the difference in days
    stack.append(i)  # Push the current day index onto the stack

print(answer)
