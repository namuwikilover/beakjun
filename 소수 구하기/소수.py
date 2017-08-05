from primesieve import *
from functools import reduce
listS=[]
for i in range(2):
    listS.append(input())
listS=list(map(int, listS))
a=generate_primes(listS[0],listS[1])
print(reduce(lambda x,y: x+y, a))
print(min(a))
