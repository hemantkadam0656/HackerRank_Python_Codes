def moveZeros(nums):
    n = len(nums)
    temp = []
    
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])
    
    for i in range(n- len(temp)):
        temp.append(0)

    for i in range(len(temp)):
        nums[i] = temp[i]
    return nums
        


if __name__ == '__main__':
    nums = [0,0]
    obj = moveZeros(nums)
    print(obj)