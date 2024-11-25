def MaxSubArraySum(arr):
    n = len(arr)
    res = arr[0]
    maxending = arr[0]

    for i in range(1,n):
        maxending = max(maxending + arr[i], arr[i])
        res = max(res, maxending)

    return res


if __name__ == '__main__':
    arr = [2,3,-8,7,-1,2,3]
    obj = MaxSubArraySum(arr)
    print(obj)