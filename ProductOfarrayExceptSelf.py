def productExceptSelf(nums):
        result = []
        prod =1    
        for i in range(len(nums)):
                prod *= nums[i]
        
        if prod != 0 :
            for j in range(len(nums)):
                result.insert(j, prod//nums[j])
        else:
            for i in range(len(nums)):
                product = 1
                for j in range(len(nums)):
                    if i == j :
                        continue
                    else:
                        product *= nums[j]  
                    
                result.insert(i, product)
        print(result)
                            
           
nums = [1,2,3,0]
productExceptSelf(nums)
