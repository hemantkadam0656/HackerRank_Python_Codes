def secondLargestNum(array):
    array.sort()
    res = []
    for i in array:
        if i not in res:
            res.append(i)

if __name__ == '__main__':
    array = list(input().split())
    secondLargestNum(array)