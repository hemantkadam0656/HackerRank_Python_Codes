arr = [2,1,6,6,6,6,3,3,3,3] 

n = len(arr)
m = n//3 

temp = []
result = []
for i in range(0, n-1):
    if arr[i] not in temp:
        temp.append(arr[i])

print(temp)

for i in range(0, len(temp)):
    count = 0
    for j in range(0, n, 1):
        if temp[i] == arr[j]:
            count += 1

    if count > m :
        result.append(temp[i])

    # result.sort()

print(result)  


