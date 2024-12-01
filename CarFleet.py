class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        
        for i in sorted(range(len(position)), key = lambda x: position[x], reverse=True):
            time = (target - position[i]) / speed[i]

            if len(fleets) == 0:
                fleets.append(time)
            
            if fleets[-1] < time:
                fleets.append(time)
                
        return len(fleets)
        
