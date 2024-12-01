def carFleet(target: int, position: list[int], speed:list[int]):
    times=[]
    for i in range(len(position)):

        time = (target - position[i]) / speed[i]
        times.append(time)
    


    return times

target = 12 
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target,position,speed))
