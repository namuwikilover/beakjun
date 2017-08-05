import sys

def Quize(string):
    c=0
    s=0
    for i in range(len(string)):
        if string[i]=='O':
            c+=1
            s+=c
        else:
            c=0
            s+=c 
    return s

n=int(input())
l=[]
for i in range(n):
    string=sys.stdin.readline()[:-1]
    b=Quize(string)
    l.append(b)
for i in l:
    print(i)    