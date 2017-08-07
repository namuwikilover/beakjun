import math
N=int(input())
if int(N%5/3)!=1:
    print('-1')
else:
    if N%5==0: print(int(N/5))
    else:
        print(int(N/5)+math.ceil(N%5/3))
