N=int(input())
if N%2==0: print('I LOVE CBNU')
else:
    for i in range(N):
        print('*', end='')
    print('\n')
    for i in range(N-2): # 삼각혁 줄 갯수.
        for j in range(N):
            print(' ', end='')
            if j==int(N/2)+i or j==int(N/2)-i:
                print('*', end='')
        print('\n')
                
    