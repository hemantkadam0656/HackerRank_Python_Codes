def swap_case(s):

    stringWords = [i for i in s]
    responce = []

    for i in stringWords:   
        if i.islower():
            responce.append(i.upper())
        elif i.isupper():
            responce.append(i.lower())
        else:
            responce.append(i)

    return "".join(responce)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)