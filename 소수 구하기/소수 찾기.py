def  isPrime(n):
    if n==1: return 0
    isPrime = 1
    for i in range(2,n):
        if n%i==0: isPrime=0

    if isPrime==1: return 1 # its' prime number
    else: return 0 # its' not prime number

N=int(input()); c=0
l=list(map(int, input().split()))
for i in range(len(l)):
    if isPrime(l[i])==1: c+=1
print(c)
