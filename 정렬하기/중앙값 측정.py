n,k=map(int,input().split())
l=[]
m=[]
s=0
for i in range(n):
    l.append(int(input()))

for j in range(n-k+1):
    for i in range(j,j+k):
        m.append(l[i])
    s+=m[(k+1)//2-1]
    m[:]=[]

print(s)

