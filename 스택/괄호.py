import sys

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

n=int(input())
l=[]
for i in range(n):
    l.append(sys.stdin.readline()[:-1])
for i in range(n):
    if matched(l[i]):
        print('YES')
    else:
        print('NO')
        
