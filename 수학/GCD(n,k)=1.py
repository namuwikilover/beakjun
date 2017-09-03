import sys

def gcd(b,s):
    if s==0: return int(b)
    else: return gcd(s,b%s)

number=int(sys.stdin.readline()[:-1])
count=0
for k in range(1,number+1):
    if gcd(number,k)==1:
        count+=1
print(count)


