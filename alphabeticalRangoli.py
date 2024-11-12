def print_rangoli(n):        
    apla = list(map(chr, range(97,123)))
    strings = []

    for i in range(n):
        string = "-".join(apla[n-1:i:-1] + apla[i:n])
        # strings.append(string.center(4 * n - 3 , '-'))  # This is in-built method to get the dash with alphabet at centre  
        strings.append(string)

    # print('\n'.join(strings[-1::-1] + strings[1:])) # This is in-built method to get the dash with alphabet at centre 


    for j in range(len(strings) - 1 , 0 , -1):
        print("-"*(2*j) + strings[j] + "-"*(2*j) )

    for j in range(len(strings)):
        print("-"*(2*j) + strings[j] + "-"*(2*j) )
    print(strings)
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)