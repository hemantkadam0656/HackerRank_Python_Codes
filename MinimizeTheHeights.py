def MinimizeTheHeights(arr, k):

    n = len(arr)
    if n == 1:
        return 0
    arr.sort()
    Tmin = arr[0]
    Tmax = arr[-1]
    height = Tmax - Tmin
    temp = []


    for i in range(1,n):
        Tmin = min(arr[0] + k, arr[i] - k)
        Tmax = max(arr[i-1] + k, arr[-1] - k)
        height = min(height, Tmax - Tmin)
    
    
    return height



if __name__ == '__main__':
    arr = [3,9,12,16,20]
    k = 3
    obj = MinimizeTheHeights(arr, k)
    print(obj)