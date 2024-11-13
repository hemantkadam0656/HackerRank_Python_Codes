def productExceptSelf(nums):    
    result = []    
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                product *= nums[j]

        result.insert(i,product)
    
    print(result)
        
            
        
        

    


# if __name__ == '__main__':
#     n = int(input())
#     nums = []
#     for i in range(n):
#         num = int(input())
#         nums.append(num)
nums = [0,0]
productExceptSelf(nums)
