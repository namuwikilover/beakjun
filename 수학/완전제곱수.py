def isSquare(number):
    return int(number**0.5)**2==number

M=int(input()); N=int(input()); l=[]

for i in range(M, N+1):
    if isSquare(i)==True: l.append(i)

if l: print(sum(l)); print(min(l))
else: print('-1')
