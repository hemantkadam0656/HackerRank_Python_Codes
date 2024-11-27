def SmallestPositiveNum(arr):
    n = len(arr)
    
    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp

    for i in range(1,n+1):
        if i != arr[i - 1]:
            return i
        
    return i

             

if __name__ == '__main__':
    arr= [2,-3,4,1,1,7]
    obj = SmallestPositiveNum(arr)
    print(obj)
