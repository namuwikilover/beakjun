def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;
N=int(input())
l=list(map(int, input().split()))
for i in range(1, N):
    if l[0]%l[i]==0: print(str(int(l[0]/l[i]))+'/1')
    else: print(str(int(l[0]/findD(l[0],l[i])))+'/'+str(int(l[i]/findD(l[0],l[i]))))