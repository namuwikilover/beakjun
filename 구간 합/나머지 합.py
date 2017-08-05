import sys

N, M = map(int, sys.stdin.readline()[:-1].split())
l=list(map(int, sys.stdin.readline()[:-1].split())); count=0

for begin in range(N):
    for end in range(N+1):
        if begin<end:
            if sum(l[begin:end])%M==0: count+=1

print(count)