def  isPrime(n):
    if n==1: return 0
    isPrime = 1
    for i in range(2,n):
        if n%i==0: isPrime=0

    if isPrime==1: return 1 # its' prime number
    else: return 0 # its' not prime number

N=int(input()); M=int(input()); l=[]
for i in range(N, M+1):
    if isPrime(i): l.append(i)
if not l: print('-1')
else: print(sum(l)); print(min(l))