def design(N,M):
    for i in range(1,N, 2):
        print((".|."*i).center(M, "-"))

    print(("welcome").center(M,"-"))

    for j in range(N-2, 0 , -2):
        print((".|."*j).center(M, "-"))

if __name__ == '__main__':
    N, M = map(int, input().split())
    if  N < 5 :
        print('Pls Enter value of N more than 5')    
    elif 3 * N == M  and N > 5:
        mat = design(N,M)
    else:    
        print('Pls Enter M value trice of N ')
    