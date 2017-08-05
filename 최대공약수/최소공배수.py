def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;

a = lambda x,y:x*y/findD(x,y)

N=int(input())
for i in range(N):
    list=[]
    list[:1]=input().split()
    print(int(a(int(list[0]),int(list[1]))))
