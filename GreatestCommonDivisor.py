
def gcdOfStrings(str1, str2 ):
        maxstr = max(str1, str2)
        minstr = min(str1, str2)  
        list = [] 
        sortstrings = []

        templist = maxstr.split(maxstr[0])

        list.append(maxstr[0])

        for i in templist[1:len(templist)]:
            if i not in list:
                list.append(i)

        substring = ''.join(list)

        for i in range(0,len(maxstr), len(substring)):
            if maxstr[i: len(substring)+i] == substring:
                sortstrings.append(maxstr[i: len(substring)+i])

        # print(minstr[0:len(substring)])

        if substring == minstr[0:len(substring)]:
            return (substring)
        else:
            return ''


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    result = gcdOfStrings(str1, str2)
    print(result)

        