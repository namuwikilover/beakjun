import re
import math
number=int(input())
def factorial(n) :
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
check=str((factorial(number)))
for i in range(int(math.log10(number))+1, 0, -1):
    if check[i]=='0':
        count+=1
    elif re.findall([1-9],check[i]):
        print(count)
# print(factorial(num))
