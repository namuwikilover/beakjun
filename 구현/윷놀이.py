l=[[0 for value in range(3)] for value in range(3)]; count=0

for i in range(3):
    l[i]=list(map(int, input().split()))

for i in range(3):
    for j in range(4):
        if l[i][j]==0: count+=1
    if count==0: print('E')
    if count==1: print('A')
    if count==2: print('B')
    if count==3: print('C')
    if count==4: print('D')
    count=0
    
