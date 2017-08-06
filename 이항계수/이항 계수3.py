import functools

@functools.lru_cache(maxsize=None)
def binomial(n, k):
    if k == n or k ==0:                         #n == k 일때 헷갈림..
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

l=[[0 for value in range(2)] for value in range(1000)]

for i in range(1000):
    l[i]=list(map(int, input().split()))
    if l[i][0]==0 and l[i][1]==0: break

print(l)

for i in range(1000):
    if l[i][0]==0 and l[i][1]==0: break
    print(binomial(l[i][0], l[i][1]))

