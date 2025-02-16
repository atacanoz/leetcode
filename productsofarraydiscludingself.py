nums = [1,2,4,6]

res = list()
right , left = 1 , 1


for i in range(len(nums)):
    res.append(right)
    right *= nums[i]
    print(res)

for k in range(len(nums)):
    res[len(nums)-k-1] *= left    
    left *= nums[len(nums)-k-1]
    print(res)
          
    

  


   
    






        

