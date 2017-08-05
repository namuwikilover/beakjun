def  isPrime(number):
    isPrime = 1
    for i in range():#숫자가 2부터 시작하게 조사.
        if number%i==0:
            isPrime=0

    if isPrime==1:
        return 1
    else:
        return 0

list = []
count = 0

for i in range(inputNumber):
    count += isPrime(list[i])

print(count)






'''
import math
count = 0

def isPrime(number) :
    isPrime = 1

    for i in range(2, int((math.sqrt(number)))):
        if number == 1: return 0
        if number%i == 0:
            isPrime = 0
    if(isPrime==1):
        return 1
    else:
        return 0

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

for j in range(N):
    k = isPrime(int(li[i]))
    if k==1: count+=1

print(count)





#print(math.sqrt(16))
'''
