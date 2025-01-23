# Binary Search Algorithm O(logn)


def BinarySearch(arr, target):
    left, right = 0, len(arr)-1

    while left <= right: 
        mid = (left + right)//2
#ajnlkhbn     
        if arr[mid]==target:    
            return mid    
        elif arr[mid]>target:            
            right = mid - 1
        else:
            left = mid + 1                   
    return -1                  
   
    


eee = [0, 1, 2, 3,  4,  5,  6,  7,  8,  9 ]
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

target = 38              

print(BinarySearch(arr,target))

y = (3 + 4 ) // 2
print(y)
