def maxSubArraySum(arr):
    n = len(arr)
    currMaxsum = 0
    currMimsum = 0
    maxSum = arr[0]
    minSum = arr[0]
    totSum =0

    for i in range(n):

        currMaxsum = max(currMaxsum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxsum)

        currMimsum = min(currMimsum + arr[i], arr[i])
        minSum = min(minSum, currMimsum)

        totSum += arr[i]

    normalSum = maxSum
    circularSum = totSum - minSum

    if minSum == totSum:
        return normalSum

    return max(normalSum, circularSum)


if __name__ == '__main__':
    arr = [8,-8,9,-9,10,-11,12]
    obj = maxSubArraySum(arr)
    print(obj)