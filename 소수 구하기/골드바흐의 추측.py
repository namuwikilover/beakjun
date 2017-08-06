def  isPrime(n):
    if n==1: return 0
    isPrime = 1
    for i in range(2,n):
        if n%i==0: isPrime=0

    if isPrime==1: return 1 # its' prime number
    else: return 0 # its' not prime number

N=int(input()); l=[]
for i in range(N):
    l.append(int(input()))
for i in range(len(l)):
    value=int(l[i]/2); j=value; k=value
    for i in range(value):
        if isPrime(j)==1 and isPrime(k)==1: break
        j+=1; k-=1
    print(k, j)
    
    

