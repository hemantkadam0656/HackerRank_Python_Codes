def issubsequesnce(s,t):
    if len(s) == 0:
        return True
    count = 0
    res = []

    for i in range(0, len(t)):
        if count < len(s):        
            if s[count] == t[i]:
                count+= 1
                res.append(t[i])

    result=  ''.join(res)

    if result == s:
        return True
    else:
        return False
if __name__ == '__main__':
    t = 'ahbgdc'
    s = ''
    obj = issubsequesnce(s,t)
    print(obj)