def increasingTriplet(nums):
    res = []
    for i in range(len(nums)-2):
        a = nums[i]
        b = nums[i +1]
        c = nums[i +2]

        if a < b < c:
            res.insert(0, True)
        else:
            res.append(False)

    if res[0] == True:
        print(True)
    else:
        print(False)
    



nums = [2,1,5,0,4,6]
obj = increasingTriplet(nums)

