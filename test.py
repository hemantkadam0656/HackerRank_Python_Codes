arr = [10,20]

count = len(arr) -1

for i in range(len(arr)):
    if i <= count:
        arr[count],arr[i] = arr[i],arr[count]
        count-=1

print(arr)