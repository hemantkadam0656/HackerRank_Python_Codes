def maximumProduct(arr):
    n = len(arr)
    leftToRight = 1
    maxProd =  float('-inf')
    rightToLeft = 1
  
    for i in range(n):
        if leftToRight == 0:
            leftToRight = 1
        if rightToLeft == 0:
            rightToLeft = 1
      
        leftToRight *= arr[i]
      
        j = n - i - 1
        rightToLeft *= arr[j]
        maxProd = max(leftToRight, rightToLeft, maxProd)
    
    print(maxProd)
        



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    maximumProduct(arr)