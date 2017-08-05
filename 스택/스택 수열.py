import sys

n=int(input())
l=[]
for i in range(n):
    l.append(int(sys.stdin.readline()))

l.reverse()
check=0
for i in range(n):
    check=l.pop()
    if l.pop()>check:
        
        
    

