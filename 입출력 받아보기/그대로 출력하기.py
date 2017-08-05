import sys
l=[]
while True:
    string=sys.stdin.readline()[:-1]
    if len(string)>0:
        l.append(string)
    else:
        break
for i in range(len(l)):
    print(l[i])
