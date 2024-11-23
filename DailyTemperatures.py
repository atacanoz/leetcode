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
