def maxArea(height):
    left, right = 0, len(height) - 1
    area = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = max(area, min_height * width) 

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area

if __name__== '__main__':
    height = [1,1]
    obj = maxArea(height)  
    print(obj)  