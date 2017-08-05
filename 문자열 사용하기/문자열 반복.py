N = int(input())

n=[0 for value in range(N)];
s=[[0 for value in range(N)] for value in range(N)];

for i in range(N):
    n[i], s[i] = input().split(); n[i]=int(n[i])

for i in range(len(n)):
    for j in range(len(s[i])):
        for k in range(n[i]):
            print(s[i][j],end='')
    print('\n')
            
