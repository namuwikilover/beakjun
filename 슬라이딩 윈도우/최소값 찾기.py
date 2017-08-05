# enter N, L 
N, L = map(int, input().split())
# enter one line and make list
l1=list(map(int, input().split()))

l2=[[0 for value in range(N)] for value in range(N)]

for i in range(N):
    for j in range(i-L+1, i+1):
        if i-L+1<=0:
            l2[i].append(l1[j])    

print(l2)


