import sys
n=int(sys.stdin.readline()); l=[] 
for i in range(n):
    l.append(sys.stdin.readline()[:-1])
l=list(set(l))
l.sort(key=lambda item:(len(item), item))
for i in l: print(i)