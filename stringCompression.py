def stringCompression(list):
    num = 0
    item = 0 
    while item < len(list):
        char = list[item]
        count = 0

        while item < len(list) and char == list[item]:
            item += 1
            count += 1
        
        list[num] = char
        num +=1 

        if count > 1:
            for i in str(count):
                list[num] = i 
                num +=1
    
    return num
              



        
    

if __name__ == '__main__':
    # array = input().split()
    array = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    obj = stringCompression(array)
    print(obj)