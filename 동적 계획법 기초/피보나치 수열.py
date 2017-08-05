import sys

zero=0
one=0

# Fibo Func
def F(n):
    if n == 0:
        global zero
        zero+=1
        return 0
    elif n == 1:
        global one
        one+=1
        return 1
    else:
        return F(n - 1) + F(n - 2)

# enter counter
c=int(input())

for i in range(c):
    n=int(sys.stdin.readline()[:-1])
    F(n)
    print(zero, one)
    zero=0
    one=0

