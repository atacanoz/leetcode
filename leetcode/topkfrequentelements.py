from collections import defaultdict
import heapq

nums = [4,4,4,2,2,2,2,2,3,7,7,7,7,7]
k = 2
out = list()
map = defaultdict(int)  
heap = []

for i in nums:
    map[i] += 1   

print(list(map.items()))
for key, value  in map.items():
    heapq.heappush(heap,(-value, key))
    print(heap)

while heap:
     value, key = heapq.heappop(heap)
     out.append(key)
     print(f"number: {key}, frequency: {-value}")


print(out)





