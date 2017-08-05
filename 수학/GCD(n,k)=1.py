def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;

number=int(input())
count=0
for k in range(1,number+1):
    if findD(number,k)==1:
        count+=1
print(count)
