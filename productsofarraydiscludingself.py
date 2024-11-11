nums = [1,2,4,6]


lst = list()

# for i ,j in range(len(nums)):
#     right = right * nums[len(nums)-1]
#     left = left * nums[i-1]
 
# for p in range(len(nums)):
#     res,right , left ,i= 1,1 , 1 , 0
#     while p + i + 1 < len(nums):
#         right = right * nums[p+i+1]
#         left = left * nums[p-i-1]
#         res = right * left * nums[p-i-1]
#         i+=1
#     lst.append(res)    

# print(lst)
  
res=1
print(len(nums))
for p in range(len(nums)):
    res *= nums[p]
    print(res)

   
    








