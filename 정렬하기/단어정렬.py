import sys
l=[]
n=int(sys.stdin.readline())
for i in range(n):
    l.append(sys.stdin.readline()[:-1])
l.sort(key=lambda item:(len(item), item))
nl=[]
[nl.append(x) for x in l if x not in l]
print(nl)
print(l)
