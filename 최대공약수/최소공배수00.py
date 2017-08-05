def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;

a = lambda x,y:x*y/findD(x,y)

listS=[]
listS[:1]=input().split()
listS=list(map(int, listS))
string1=''
string2=''
for i in range(listS[0]):
    string1[i]='1'
for i in range(listS[1]):
    string2[i]='1'
strin1=int(string1)
strin2=int(string2)
print(string1)
print(string2)
print(findD(string1,string2))


# print(int(a(int(list[0]),int(list[1]))))
