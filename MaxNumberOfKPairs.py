def maxNumberOfKPairs(arr, k,):
    count = 0
    n = len(arr)
    i = 0 
    j = n

    if len(arr) < 2 and arr[0] == k:
        return 1
    
    if len(arr) < 2 and arr[0] != k:
        return 0 

    first_num = sec_num = 0
    while i < j: 

        if arr[i] <= k:
            first_num = arr[i]
        i += 1 

        if arr[j-1] <= k:
            sec_num = arr[j-1]
        j -= 1
       
        if first_num + sec_num == k :
            count +=1



    return count





if __name__ == '__main__':
    arr = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    k = 2
    obj = maxNumberOfKPairs(arr, k)
    print(obj)


 