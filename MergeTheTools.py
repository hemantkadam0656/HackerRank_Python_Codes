def merge_the_tools(string, k):

    strlist = [i for i in string]
    result = []
    list =[]
    for i in range(0, len(string), k):
        substring = ''.join(string[j] for j in range(i, min(i+k, len(string))))
        

    print(substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)