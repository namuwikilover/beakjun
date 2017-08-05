import sys
string=sys.stdin.readline()[:-1]
l=[]
for i in string:
    l.append(i)
l.sort(reverse=True)
for i in l:
    print(i,end='')