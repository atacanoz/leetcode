# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, 

# Both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

def carFleet(target: int, position: list[int], speed:list[int]):

    times=[] 
    
    for i in sorted(range(len(position)), key=lambda x: position[x], reverse=True):
        time = (target - position[i]) / speed[i]
        if len(times) == 0:
            times.append(time)

        if times[-1] < time:
            times.append(time)   
    
    return len(times)

target = 12 
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(sorted(range(len(position)), key=lambda x: position[x], reverse=True))

y = carFleet(target,position,speed)
print(y)