def isSquare(number):
    return int(number**0.5)**2==number

ar=input().split()
n1=int(ar[0])
n2=int(ar[1])

l=[]
for i in range(n1, n2+1):
    if isSquare(i)==True:
        l.append(i)
print(l)
if l:
    print(sum(l))
    print(min(l))
else:
    print('-1')
