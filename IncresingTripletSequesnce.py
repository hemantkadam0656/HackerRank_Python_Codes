def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    
    for num in nums:
        if num <= first :
            print(num, first)
            first = num
        elif num <= second :
            second = num
        else:
            return True
            
    return False 

    

nums = [2,1,5,0,4,6]
obj = increasingTriplet(nums)
print(obj)

