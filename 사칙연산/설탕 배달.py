N=int(input())
if N%5!=0:
Check=N%5
elif Check%3!=0:
        print('-1')
else: print(int(N/5)+int(N%5/3))
