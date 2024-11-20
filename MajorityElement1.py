def MajorityElement(arr):
    n = len(arr)

    ele1, ele2 = -1,-1
    count1, count2 = 0, 0

    for i in arr:
        if i == ele1:
            count1 += 1
        elif i == ele2:
            count2 += 1
        elif count1 == 0:
            ele1 = i
            count1 +=1
        elif count2 == 0:
            ele2 = i
            count2 +=1
        else:
            count1 -=1
            count2 -=1

    res = []
    count1, count2 = 0,0
    
    for i in arr:
        if ele1 == i:
            count1 +=1
        elif ele2 == i:
            count2 +=1

    

    if count1 > n/3 :
        res.append(ele1)
    if count2 > n/3 and ele1 != ele2:
        res.append(ele2)


    if len(res)==2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res


if __name__ == '__main__':
    arr = [1,2,3,6,6,6,6,5,5,5,5]
    obj = MajorityElement(arr)
    print(obj)