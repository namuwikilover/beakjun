def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;

a = lambda x,y:x*y/findD(x,y)

list=[]
list[:1]=input().split()
print(findD(int(list[0]),int(list[1])))
print(int(a(int(list[0]),int(list[1]))))
