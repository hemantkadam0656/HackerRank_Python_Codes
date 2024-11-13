def reverseWorlds(s):
    words = s.split()
    print(words)

    string = words[::-1]
    result = " ".join(string)
    print(result)



if __name__ == '__main__':
    s = input()
    reverseWorlds(s) 