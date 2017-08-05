from functools import reduce

A, B = map(int, input().split()); l=[]

x=B-A

for i in range(x):
    l.append('1')
    
s=reduce(lambda x,y: x+str(y), l, '')
print(int(s))