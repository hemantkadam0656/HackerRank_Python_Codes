def minion_game(string): #BANANA
    listString = [i for i in string] # ['B', 'A', 'N', 'A', 'N', 'A']
    vowels = ['A','E','I','O','U']
    stuart = []
    count = 0
    stuart.append(listString[0])
    kevin = []
    for i in listString:
        if kevin == []:
            for j in vowels:
                if i == j:
                    kevin.append(i)
                    break
                else:
                    continue
    # for i in range(1,len(string)):
        
     

if __name__ == '__main__':
    s = input()
    minion_game(s)