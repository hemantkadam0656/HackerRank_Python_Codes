def rotatearray(arr, d):
    n = len(arr)

    d %= n 
    
    temp = [0] * n

    for i in range(n-d):
        temp[i] = arr[d+i]
    
    for i in range(d):
        temp[n-d+i] = arr[i]

    for i in range(n):
        arr[i] = temp[i]

    return arr


if __name__ == '__main__':
    array = [7,3,9,1]
    d = int(input())
    obj = rotatearray(array, d)
    print(obj)
