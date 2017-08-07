N=int(input()); l=[]; d=[0 for value in range(20)]
for i in range(N): l.append(int(input()))
for i in range(N):
    if i==0: d[i]=0
    elif i==1: d[i]=l[0]
    elif i==2: d[i]=l[1]+l[0]
    else: d[i]=max(l[i]+d[i-2], l[i]+d[i-1]+d[i-3])

print(d)
# print(max(2, 5))
