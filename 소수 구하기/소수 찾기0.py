from primesieve import *
a=generate_primes(40)
listS=[]
number=int(input())
listS[:2]=input().split()
listS=list(map(int, listS))
count=0
for i in range(len(listS)):
    if listS[i] in a:
        count+=1
print(count)
