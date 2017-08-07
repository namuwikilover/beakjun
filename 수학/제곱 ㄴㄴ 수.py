def isSquare(number):
    return int(number**0.5)**2==number

min, max=map(int, input().split()); c=0
for i in range(min, max+1):
    if isSquare(i)==False: c+=1
print(c)
