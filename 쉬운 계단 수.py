N=int(input()); s=0; d=[[0 for value in range(101)] for value in range(10)]

for i in range(10):
    if i==0: d[1][0]=0
    else: d[1][i]=1

for i in range(2, N+1):
    for j in range(10):
        d[i][j]=j
        if j==0: d[i-1][j+1]
        elif j==9: d[i-1][j-1]
        else: d[i][j]=((d[i-1][j-1])%1000000000+(d[i-1][j+1])%1000000000)

for i in range(10):
    s+=d[N][i]%1000000000
    s%=1000000000
print(s)
    
